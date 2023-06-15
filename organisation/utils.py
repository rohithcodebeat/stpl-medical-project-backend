from enum import Enum


class OrganisationTypeEnumType(Enum):
    DIAGNOSIS = "DIAGNOSIS"
    HOSPITAL = "HOSPITAL"
    OTHER = "OTHER"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]