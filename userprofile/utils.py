from enum import Enum


class GenderTypeEnumType(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class BloodGroupTypeEnumType(Enum):
    O_POSITIVE = "O_POSITIVE"
    O_NEGITIVE = "O_NEGITIVE"
    A_POSITIVE = "A_POSITIVE"
    A_NEGITIVE = "A_NEGITIVE"
    B_POSITIVE = "B_POSITIVE"
    B_NEGITIVE = "B_NEGITIVE"
    AB_POSITIVE = "AB_POSITIVE"
    AB_NEGITIVE = "AB_NEGITIVE"
    OTHERS  = "OTHERS"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]