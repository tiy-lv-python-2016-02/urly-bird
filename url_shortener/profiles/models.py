from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    @property
    def bookmark_count(self):
        return self.user.bookmark_set.count()
