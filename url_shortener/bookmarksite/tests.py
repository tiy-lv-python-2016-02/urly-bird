import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from hashids import Hashids
from faker import Faker

from bookmarksite.models import Bookmark, Click


class BookmarkTests(TestCase):

    def setUp(self):
        fake = Faker()
        self.user = User.objects.create_user(username=fake.name(),
                                             email=fake.email(),
                                             password="blahblah"
                                             )
        self.bookmark = Bookmark.objects.create(title=fake.bs(),
                                                url=fake.url(),
                                                user=self.user
                                                )
        self.clicks = [
            Click.objects.create(user=self.user, bookmark=self.bookmark)
            for _ in range(3)
            ]

    def test_short_url(self):
        hashid = Hashids()
        hash_url = "b/{}".format(hashid.encode(self.bookmark.id))
        self.assertEqual(hash_url, self.bookmark.short_url,
                         msg="Hashed url incorrect")

    def test_click_count(self):
        self.assertEqual(self.bookmark.click_count, 3,
                         msg="Click count incorrect")

    def test_month_count(self):
        one_year_ago = timezone.now() - datetime.timedelta(days=365)
        self.clicks[2].created_at = one_year_ago
        self.clicks[2].save()
        self.assertEqual(self.bookmark.month_count, 2,
                         msg="Month count incorrect")
