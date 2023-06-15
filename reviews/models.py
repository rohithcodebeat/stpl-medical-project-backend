from django.db import models
from django.contrib.auth import get_user_model
from organisation.models import OrganisationModel, OrganisationDoctorModel
# Create your models here.

class ReviewModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="ReviewModel_user")
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=1)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewOrganisationModel(models.Model):
    organisation = models.ForeignKey(OrganisationModel, on_delete=models.CASCADE, related_name="ReviewOrganisationModel_organisation") 
    reviews = models.ManyToManyField(ReviewModel, related_name="ReviewOrganisationModel_reviews", blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewOrganisationDoctorModel(models.Model):
    doctor = models.ForeignKey(OrganisationDoctorModel, on_delete=models.CASCADE, related_name="OrganisationDoctorModel")
    reviews = models.ManyToManyField(ReviewModel, related_name="ReviewOrganisationDoctorModel_reviews", blank=True)    

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


