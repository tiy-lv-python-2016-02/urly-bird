from django.contrib.auth.models import User
from django.db import models
from hashids import Hashids


class Bookmark(models.Model):

    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    # def get_absolute_url(self):
    #     return reverse('', args=[str(self.id)])

    def get_hash_id(self):
        hash_id = Hashids()
        return hash_id.encode(self.id)

    def click_total(self):
        return self.click_set.count()

    def __str__(self):
        return "{} saved a bookmark: {}".format(self.user.username, self.title)


class Click(models.Model):

    bookmark = models.ForeignKey(Bookmark)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(User, null=True, blank=True)


    # When a
    # user - - anonymous or logged in -- uses
    # a bookmark URL, record that
    # user, bookmark, and timestamp.A
    # suggested
    # name
    # for this model is Click, even though you can navigate to the URL
    # without a click by entering it in your navigation bar.

