from django.contrib import admin
from .models import UserProfileMediaGalleryModel,UserProfileModel,UserCartModel
# Register your models here.
admin.site.register(UserProfileMediaGalleryModel)
admin.site.register(UserProfileModel)
admin.site.register(UserCartModel)