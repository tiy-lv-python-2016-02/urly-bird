from hashids import Hashids

from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)

    @property
    def hash_id(self):
        hashid = Hashids()
        return hashid.encode(self.id)

    @property
    def short_url(self):
        return "b/{}".format(self.hash_id)

    @property
    def click_count(self):
        return self.click_set.count()

    def __str__(self):
        return self.title


class Click(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    bookmark = models.ForeignKey(Bookmark)
    user = models.ForeignKey(User)
