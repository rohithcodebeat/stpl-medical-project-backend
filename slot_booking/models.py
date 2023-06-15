from django.db import models
from django.contrib.auth import get_user_model
from organisation.models import OrganisationDoctorModel
from .utils import SlotBookingStatusTypeEnumType, SlotBookingRecordTypeEnumType
# Create your models here.

class SlotBookingRecordMediaModel(models.Model):
    record_type = models.CharField(max_length=50, choices=SlotBookingRecordTypeEnumType.choices(), null=True, blank=True)
    media = models.URLField(max_length=1000, null=True, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class OrganisationSlotBookingModel(models.Model):
    booking_id = models.CharField(max_length=100)
    doctor = models.ForeignKey(OrganisationDoctorModel, on_delete=models.CASCADE, related_name="OrganisationSlotBookingModel_doctor")
    date = models.DateField(null=True, blank=True)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    is_booked = models.BooleanField(default=True)
    record = models.ManyToManyField(SlotBookingRecordMediaModel, related_name="OrganisationSlotBookingModel_media", blank=True)
    booking_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="OrganisationSlotBookingModel_booking_user", null=True, blank=True)
    status = models.CharField(max_length=100, choices=SlotBookingStatusTypeEnumType.choices(),default="PENDING")



    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

"""
Booking Id DATETIME extract only number
2006-10-25 14:30:59 -> 20061025143059

logic
from datetime import datetime
dt = datetime.now()
id = "SLOTID"+str(dt.year)+str(dt.month)+str(dt.day)+str(dt.hour)+str(dt.minute)+str(dt.second)+str(dt.microsecond)
'SLOTID20236151726405519'
"""

class OrderModel(models.Model):
    booking_id = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="OrderModel_user")
    items = models.ManyToManyField(OrganisationSlotBookingModel, related_name="OrderModel_items", blank=True)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)




"""
Order Id DATETIME extract only number
2006-10-25 14:30:59 -> 20061025143059

logic
from datetime import datetime
dt = datetime.now()
id = "ORDERID"+str(dt.year)+str(dt.month)+str(dt.day)+str(dt.hour)+str(dt.minute)+str(dt.second)+str(dt.microsecond)
'ORDERID20236151726405519'
"""