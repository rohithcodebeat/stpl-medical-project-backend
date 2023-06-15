from django.db import models
from django.contrib.auth import get_user_model
from .utils import GenderTypeEnumType, BloodGroupTypeEnumType
from slot_booking.models import OrganisationSlotBookingModel
# Create your models here.

class UserProfileMediaGalleryModel(models.Model):
    media = models.URLField(max_length=1000, null=True, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="UserProfileModel_user")
    profile_pics = models.URLField(max_length=1000, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=25, choices=GenderTypeEnumType.choices(), null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    blood_group = models.CharField(max_length=25, choices=BloodGroupTypeEnumType.choices(), null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UserCartModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="UserCartModel_user")
    slot = models.ManyToManyField(OrganisationSlotBookingModel, related_name="UserCartModel_slot", blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)