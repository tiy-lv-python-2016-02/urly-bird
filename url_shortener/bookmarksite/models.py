import datetime

from hashids import Hashids

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Bookmark(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)

    @property
    def hash_id(self):
        """
        :return: A reversible, unique, encoded value based on the bookmark's
        unique id.
        """
        hashid = Hashids()
        return hashid.encode(self.id)

    @property
    def short_url(self):
        """
        This is the shortened url that is associated with the bookmark, used
        for display purposes.
        The hashid will not change but the 'b/' is copied from urls.py
        and would need to be changed manually if the url scheme changes.
        """
        return "b/{}".format(self.hash_id)

    @property
    def click_count(self):
        """
        :return: A straightforward count of how many clicks a bookmark has.
        """
        return self.click_set.count()

    @property
    def month_count(self):
        """
        :return: The number of clicks recieved in that past 30 days.
        """
        one_month_ago = timezone.now() - datetime.timedelta(days=30)
        return self.click_set.filter(created_at__gte=one_month_ago).count()

    def __str__(self):
        return self.title


class Click(models.Model):
    """
    The user field is left blank when the click is created by an
    anonymous user of the site.
    """
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    bookmark = models.ForeignKey(Bookmark)
    user = models.ForeignKey(User, null=True, blank=True)
