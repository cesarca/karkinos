from datetime import datetime
from operator import attrgetter
from constants import TUMOR_PHENOTYPE, BENIGN_TUMOR, TYPE_OF_TUMOR, POLIPO_DE_COLON, LYNCH_TUMORS, \
    POLIPOS, POLIPOSIS_ADENOMATOSA_FAMILIAR, APC, CANCER_DE_OVARIO, CANCER_DE_MAMA, CANCER_DE_MAMA_BILATERAL


class Karkinos:
    def __init__(self, patient):
        self.echnd = ECHND(patient.relatives)
        self.garner = Garner(patient.relatives)
        self.paf = PAF(patient.relatives)
        self.pafa = PAFA(patient.relatives)

    def search_most_young_phenotype(self, relatives):
        return next(r for r in sorted(relatives, key=attrgetter('birth_date')) if r.has_tumor)

    def index_case(self, relatives):
        for relative in relatives:
            if relative.has_tumor:
                if self.tumors_has_type(relative.tumors, TUMOR_PHENOTYPE):
                    return relative
                else:
                    return self.search_most_young_phenotype(relatives)
        return None

    def tumors_has_type(self, tumors, type_searched):
        for t in tumors:
            if t.tumor_type_name == type_searched:
                return True
        return False


class ECHND:
    def __init__(self, relatives):
        self.relatives = relatives

    def get_echnd_informative(self):
        if self.__patients_with_more_age_than(3, 65):
            return True
        elif self.__number_of_patients_with_tumor_type(3, TYPE_OF_TUMOR):
            if self.__patients_with_more_age_than(1, 50) and PAF(self.relatives).get_paf_diagnosis():
                return True
            else:
                return False
        else:
            if self.__tumor_type_and_class_before_age(TYPE_OF_TUMOR, POLIPO_DE_COLON,
                                                      50) or self.__patients_with_lynch_tumors():
                return True
            return False

    def __patients_with_more_age_than(self, n, age):
        return len([r for r in self.relatives if (datetime.datetime.now().year() - r.birth_date.year()) >= age]) > n

    def __patients_with_less_age_than(self, n, age):
        return len([r for r in self.relatives if (datetime.datetime.now().year() - r.birth_date.year()) < age]) > n

    def __number_of_patients_with_tumor_type(self, n, type_tumor_name):
        return len(
            [r for r in self.relatives if len([t for t in r.tumors if t.tumor_type_name == type_tumor_name]) >= 1]) >= n

    def __tumor_type_and_class_before_age(self, tumor_type, tumor_class, age):
        return len([r for r in self.relatives if len(
            [t for t in r.tumors if t.tumor_type_name == tumor_type and t.name == tumor_class] and (
                datetime.datetime.now().year() - r.birth_date.year()) < age) >= 1])

    def __patients_with_lynch_tumors(self):
        return len([r for r in self.relatives if
                    len([t for t in r.tumors if t.tumor_type_name in LYNCH_TUMORS]) >= 1]) >= 1 or PAF(
            self.relatives).get_paf_diagnosis()


class Garner:
    def __init__(self, relatives):
        self.relatives = relatives

    def get_informatives(self):
        return self.__garner()

    def get_asociated(self):
        return self.__garner()

    def has_garner(self):
        return True if len(self.__garner()) >= 1 else False

    def __has_paf_and_benign(self, r):
        typeoftumor = next(tumor for tumor in r.tumors if tumor.tumor_type_name == TYPE_OF_TUMOR and tumor.name.find(
            POLIPOSIS_ADENOMATOSA_FAMILIAR) != -1)
        benigntumor = next(tumor for tumor in r.tumors if tumor.tumor_type_name == BENIGN_TUMOR)
        return (typeoftumor and benigntumor) is not None

    def __garner(self):
        return [r for r in self.relatives if len(r.tumors) >= 2 and self.__has_paf_and_benign(r)]


class PAF:
    def __init__(self, relatives):
        self.relatives = relatives

    def get_paf_informatives(self):
        return [r for r in self.relatives if self.__has_mutation(r) or self.__is_paf_informative(r)]

    def get_paf_associated_cases(self):
        return self.get_paf_informatives()

    def __has_mutation(self, relative):
        return True if self.__tumors_has_type_and_name(relative.tumors, TYPE_OF_TUMOR, APC) else False

    def __tumors_has_type_and_name(self, tumors, type_searched, tumor_name):
        for t in tumors:
            if t.tumor_type_name == type_searched and t.name.find(tumor_name) != -1:
                return True
        return False

    def __is_paf_informative(self, relative):
        for tumor in relative.tumors:
            if tumor.tumor_type_name == TYPE_OF_TUMOR and tumor.name.find(POLIPOS) != -1 and tumor.npolyps >= 100:
                return True
        return False

    def get_paf_diagnosis(self):
        return True if len([r for r in self.relatives if self.__is_paf_informative(r)]) >= 1 else False


class PAFA:
    def __init__(self, relatives):
        self.relatives = relatives

    def get_pafa_informatives(self):
        return [r for r in self.relatives if not self.__has_mutation(r) or self.__is_pafa_informative(r)]

    def get_pafa_associated_cases(self):
        return self.get_pafa_informatives()

    def __has_mutation(self, relative):
        return True if self.__tumors_has_type_and_name(relative.tumors, TYPE_OF_TUMOR, APC) else False

    def get_pafa_diagnosis(self):
        return True if len([r for r in self.relatives if self.__is_pafa_informative(r)]) >= 1 else False

    def __tumors_has_type_and_name(self, tumors, type_searched, tumor_name):
        for t in tumors:
            if t.tumor_type_name == type_searched and t.name.find(tumor_name) != -1:
                return True
        return False

    def __is_pafa_informative(self, relative):
        for tumor in relative.tumors:
            if tumor.tumor_type_name == TYPE_OF_TUMOR and tumor.name.find(POLIPOS) != -1 and tumor.npolyps in range(
                    20, 101):
                return True
        return False


class CMOH:
    def __init__(self, relatives):
        self.relatives = relatives

    def is_informative(self):
        if self.__more_women_with_more_ages(3, 65):
            return True
        elif self.__more_tumor_has_list_type_and_name_than(TYPE_OF_TUMOR, [CANCER_DE_MAMA, CANCER_DE_OVARIO], 2):
            if self.__tumors_has_name_and_age_less_than(CANCER_DE_MAMA_BILATERAL, 50) or self.__tumors_has_name_and_age_less_than(CANCER_DE_MAMA, 50):
                return True
            return False
        else:
            if (alguna de estas otras):
                return True
            return False

    def __more_women_with_more_ages(self, num_women, age):
        return len([r for r in self.relatives if
                    (datetime.datetime.now().year() - r.birth_date.year()) >= age and r.gender == 'Mujer']) >= num_women

    def __more_women_with_more_ages_and_tumor_name(self, num_women, age, tumor_name):
        return len([r for r in self.relatives if
                    (datetime.datetime.now().year() - r.birth_date.year()) >= age and r.gender == 'Mujer'
                    and self.__tumors_has_name(r.tumors, tumor_name)]) >= num_women

    def __more_tumor_has_list_type_and_name_than(self, type_searched, tumor_name, nrelatives):
        return len(
            [r for r in self.relatives if self.__tumors_has_alistof_type_and_name(type_searched, tumor_name)]) >= nrelatives

    def __tumors_has_alistof_type_and_name(self, tumors, type_searched, tumor_name):
        for t in tumors:
            if t.tumor_type_name == type_searched and (
                    t.name.find(tumor_name[0]) != -1 or t.name.find(tumor_name[1]) != -1):
                return True
        return False

    def __tumors_has_name(self, tumors, tumor_name):
        for t in tumors:
            if t.name == tumor_name and (t.name.find(tumor_name) != -1):
                return True
        return False

