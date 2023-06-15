from enum import Enum


class SlotBookingStatusTypeEnumType(Enum):
    PENDING = "PENDING"
    UPCOMING = "UPCOMING"
    COMPLETE = "COMPLETED"
    FAILED = "FAILED"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class SlotBookingRecordTypeEnumType(Enum):
    REPORT = "REPORT" 
    PRESCRIPTION = "PRESCRIPTION"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]