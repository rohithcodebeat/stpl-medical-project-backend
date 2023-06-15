from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid 
from django.contrib.auth import get_user_model
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email, username,phone_number, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        This Create Method is regular user, Or Website register method
        """
        if not email:
            raise ValueError('The Email field must be set')
        uuid_id = uuid.uuid1()
        email = self.normalize_email(email)
        user = self.model(id=uuid_id,email=email, username=username, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_employee(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        uuid_id = uuid.uuid1()
        email = self.normalize_email(email)
        user = self.model(id=uuid_id,email=email, **extra_fields)
        extra_fields.setdefault('is_staff', True)
        user.is_employee = True 
        return user 

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_employee', True)
        extra_fields.setdefault('is_instructor', True)
        name = str(email)
        namespace_uuid = uuid.NAMESPACE_X500
        uuid_id = uuid.uuid5(name=name, namespace=namespace_uuid)
        user = self.model(id=uuid_id,email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 



# from django.contrib.auth.models import User 
class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    country_code = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    is_already_login = models.BooleanField(default=False, null=True, blank=True)
    
    # Permissions
    is_instructor = models.BooleanField(default=False, null=True, blank=True)
    is_staff = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_employee = models.BooleanField(default=False, null=True, blank=True)
    

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email




class OtpVerifyModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="EmailOtpVerifyModel_user")
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, unique=True)

    otp = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)