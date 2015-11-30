_READ_ERROR_MESSAGE = "Error al leer la edad de diagnostico"

from constants import TUMOR_PHENOTYPE, TYPE_OF_TUMOR, BENIGN_TUMOR, NO_TUMOR


class Tumor:
    def __init__(self, tumor_xml):
        self.age = self.read_diagnosis_age(tumor_xml)
        self.tumor_type_name, self.tumor_type = self.get_tumor_type(tumor_xml)
        self.name = self.read_tumor_name()
        self.code = self.read_tumor_code()
        self.npolyps = self.read_number_of_polyps_ifneeded()

    def get_tumor_type(self, tumor_xml):
        try:
            return TYPE_OF_TUMOR, tumor_xml.TypeOfTumor
        except:
            try:
                return TUMOR_PHENOTYPE, tumor_xml.TumorPhenotype
            except:
                try:
                    return BENIGN_TUMOR, tumor_xml.BenignTumor
                except:
                    return NO_TUMOR, None

    def read_diagnosis_age(self, tumor_xml):
        try:
            return tumor_xml.AgeOfDiagnosis.Age.Value
        except:
            print _READ_ERROR_MESSAGE

    def read_tumor_code(self):
        return self.tumor_type.Description.Code.Value

    def read_tumor_name(self):
        return self.tumor_type.Description.Text

    def read_number_of_polyps_ifneeded(self):
        try:
            return self.tumor_type.Description.NPolyps
        except:
            return 0
