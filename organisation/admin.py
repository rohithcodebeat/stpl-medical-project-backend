from django.contrib import admin
from .models import CategoryModel,OrganisationMediaGalleryModel,OrganisationModel,OrganisationCategoryModel,OrganisationDoctorModel,OrganisationCategoryDescriptionModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(OrganisationMediaGalleryModel)
admin.site.register(OrganisationModel)
admin.site.register(OrganisationCategoryDescriptionModel)
admin.site.register(OrganisationCategoryModel)
admin.site.register(OrganisationDoctorModel)
