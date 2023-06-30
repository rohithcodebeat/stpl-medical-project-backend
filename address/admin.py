from django.contrib import admin
from .models import CountryModel,StateModel,CityModel,AddressModel
# Register your models here.
admin.site.register(CountryModel)
admin.site.register(StateModel)
admin.site.register(CityModel)
admin.site.register(AddressModel)