import datetime
from django.contrib.auth.models import User
from django.db import models
from hashids import Hashids
from django.utils import timezone


class Bookmark(models.Model):
    """
    Bookmark model
    with fields: url, title, description, user
    has created_at & modified_at attributes
    methods:
    *get_hash_id -- encodes the bookmark
    id into a hash_id
    *click_total -- returns the count from click_set
    *month_clicks -- returns click_set count for the last 30 days
    """
    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def get_hash_id(self):
        hash_id = Hashids()
        return hash_id.encode(self.id)

    @property
    def click_total(self):
        return self.click_set.count()

    @property
    def month_clicks(self):
        """
        month_from_now variable that is set to the time 30 days ago
        returns the number of clicks for the month
        """
        month_from_now = timezone.now() - datetime.timedelta(days=30)
        return len(self.click_set.filter(created_at__gte=month_from_now))

    def __str__(self):
        return "{} saved bookmark: {}".format(self.user.username, self.title)


class Click(models.Model):
    """
    Click model
    created when user uses an UrlyBird shortened
    URL.
    stores which bookmark, user (blank/null if anonymous or logged in)
    + created_at
    """

    bookmark = models.ForeignKey(Bookmark)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(User, null=True, blank=True)
