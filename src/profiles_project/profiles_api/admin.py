from django.contrib import admin
#  WE NEED TO REGISTER MODELS HERE
from . import models
# Register your models here.
#  then user model will be populated in admin pannel
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeed)