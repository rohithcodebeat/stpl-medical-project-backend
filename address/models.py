from django.db import models

# Create your models here.
class CountryModel(models.Model):
    title = models.CharField(max_length=200)


    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class StateModel(models.Model):
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name="StateModel_country")
    title = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class CityModel(models.Model):
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name="CityModel_country")
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="CityModel_state")
    title = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)



class AddressModel(models.Model):
    address_1 = models.CharField(max_length=300, null=True, blank=True)
    address_2 = models.CharField(max_length=300, null=True, blank=True)
    x_coordinate = models.CharField(max_length=100, null=True, blank=True)
    y_coordinate = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="AddressModel_city", null=True, blank=True)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="AddressModel_state", null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name="AddressModel_country", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)