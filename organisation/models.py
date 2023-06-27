from django.db import models
from django.contrib.auth import get_user_model
from address.models import AddressModel
from .utils import OrganisationTypeEnumType
# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    icon = models.URLField(max_length=1000, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class OrganisationMediaGalleryModel(models.Model):
    media = models.URLField(max_length=1000, null=True, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



class OrganisationModel(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    sub_title = models.CharField(max_length=500, null=True, blank=True)
    profile = models.URLField(max_length=1000, null=True, blank=True)
    media = models.ManyToManyField(OrganisationMediaGalleryModel, related_name="OrganisationModel_media", blank=True)
    description = models.TextField(null=True, blank=True)
    org_type = models.CharField(max_length=100, choices=OrganisationTypeEnumType.choices(), null=True, blank=True)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, related_name="OrganisationModel_address", blank=True, null=True)

    x_coordinate = models.CharField(max_length=100, null=True, blank=True)
    y_coordinate = models.CharField(max_length=100, null=True, blank=True)

    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class OrganisationCategoryDescriptionModel(models.Model):
    description = models.TextField(null=True, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



class OrganisationCategoryModel(models.Model):
    organisation = models.ForeignKey(OrganisationModel, on_delete=models.CASCADE, related_name="OrganisationCategoryModel_organisation", null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    sub_title = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="OrganisationCategoryModel_category")
    media = models.ManyToManyField(OrganisationMediaGalleryModel, related_name="OrganisationCategoryModel_media", blank=True)
    icon = models.ForeignKey(OrganisationMediaGalleryModel, on_delete=models.CASCADE,related_name="OrganisationCategoryModel_icon", blank=True, null=True)
    description = models.ManyToManyField(OrganisationCategoryDescriptionModel, related_name="OrganisationCategoryModel_description", blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class OrganisationDoctorModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="OrganisationDoctorModel_user") # Doctor
    category = models.ForeignKey(OrganisationCategoryModel, on_delete=models.CASCADE, related_name="OrganisationDoctorModel_category", null=True, blank=True)
    price = models.DecimalField(decimal_places=4, max_digits=10,null=True, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

