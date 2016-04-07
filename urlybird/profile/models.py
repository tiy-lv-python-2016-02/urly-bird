from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    OneToOneField with User model
    image field @ image uploads to media/profilepicture folder
    interests field (details entered into this field arent currently being
    displayed on public profile)
    both image and interests can be left blank
    Profile model is created when User registers
    """

    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='profilepicture/', null=True, blank=True)
    interests = models.CharField(max_length=2000, blank=True, null=True)


