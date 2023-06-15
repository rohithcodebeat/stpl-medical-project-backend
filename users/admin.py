from django.contrib import admin
from users.models import UserModel, OtpVerifyModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(OtpVerifyModel)