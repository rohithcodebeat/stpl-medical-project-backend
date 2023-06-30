from django.contrib import admin
from .models import ReviewModel,ReviewOrganisationDoctorModel,ReviewOrganisationModel
# Register your models here.
admin.site.register(ReviewModel)
admin.site.register(ReviewOrganisationModel)
admin.site.register(ReviewOrganisationDoctorModel)