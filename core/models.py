from django.db import models

# Create your models here.
class Profile(models.Model):
    user = pass
    id_user = pass
    bio = pass
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = pass