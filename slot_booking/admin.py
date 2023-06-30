from django.contrib import admin
from .models import SlotBookingRecordMediaModel,OrganisationSlotBookingModel,OrderModel
# Register your models here.
admin.site.register(SlotBookingRecordMediaModel)
admin.site.register(OrganisationSlotBookingModel)
admin.site.register(OrderModel)