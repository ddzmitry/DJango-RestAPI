from django.db import models
# import user model
from django.contrib.auth.models import AbstractBaseUser
# get promision mixin
from django.contrib.auth.models import PermissionsMixin
# get userManagegr
from django.contrib.auth.models import BaseUserManager
# Create your models here.
# sub user model
#  Override User and UserManager here 
class UserProfileManager(BaseUserManager):
    """Helps Django work with customer user model"""
    def create_user(self,email,name,password=None):
        """Create a new user profile object"""
        if not email:
            raise ValueError('User must have an email adress.')
        # normilizing email
        email = self.normalize_email(email)
        # create user
        user = self.model(email=email,name=name)
        # set password and encrypt
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password):
        """Creates and saves a new superuser with given details"""
        user = self.create_user(email,name,password)
        # give superuser premissions here
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin): 
    # """
    # Represent User profile inside of the system
    # """
    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #  object manager to manage user profiles requierd
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    # define required fields
    REQUIRED_FIELDS = ['name']
    # custom funciton
    def get_full_name(self):
        """Used to get a user fullname"""
        return self.name

    def get_short_name(self):
        """Used to get users short name"""
        return self.name
    # ti return user profile as a string
    def __str__(self):
        """Django uses this when need to convert object to a string"""
        return self.email

# create feed
class ProfileFeed(models.Model):
    
    """Profile Status Update"""
    # foreign key to track user
    # if user deleted will delete all statuses
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    # adding current time
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.status_text