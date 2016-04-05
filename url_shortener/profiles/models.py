from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)

    image = models.ImageField(upload_to="profile/", null=True, blank=True)
