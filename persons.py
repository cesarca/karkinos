from datetime import datetime
from tumor import Tumor


class Patient:
    def read_patient_tumors(self, xml):
        tumors = []
        for tumor in xml.Body.Tumors.Tumor:
            t = Tumor(tumor)
            tumors.append(t)
        return tumors

    def __init__(self, xml):
        self.age = xml.Body.HealthStatusActor.DateTime.Age.Value
        self.has_tumor = xml.Body.HealthStatusActor.PresenceOfTumor
        self.status = xml.Body.HealthStatusActor.Description.Text
        self.tumors = self.read_patient_tumors(xml)
        self.relatives = self.read_relatives(xml)

    def read_relatives(self, xml):
        relatives = []
        for relative in xml.Actors.Actor:
            a = Relative(relative, xml)

            relatives.append(a)

        return relatives


class Relative:
    def read_relative_tumors(self, xml):
        tumors = []

        for tumor in xml.Body.FamilyHistory.FamilyTumorHistory:
            if tumor.FamilyMember.ActorID == self.actor_obj_id and \
                            tumor.FamilyMember.HealthStatusActor.PresenceOfTumor == "Si":
                for tmr in tumor.Tumor:
                    t = Tumor(tmr)
                    tumors.append(t)
        return tumors

    def __init__(self, actor, xml):
        self.actor_obj_id = actor.ActorObjectID
        self.display_name = actor.Person.Name.DisplayName
        self.birth_date = datetime.strptime(str(actor.Person.DateOfBirth.ExactDateTime), '%Y-%m-%d')
        self.gender = actor.Person.Gender.Text
        self.gender_code = actor.Person.Gender.Code.Value
        self.relation = actor.Relation.Text
        self.tumors = self.read_relative_tumors(xml)
        self.has_tumor = len(self.tumors) > 0
