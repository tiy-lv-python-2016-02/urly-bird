from django.test import TestCase

import datetime
from django.test import TestCase
from urlsandbookmarks.models import Bookmark, Click
from django.contrib.auth.models import User
from django.utils import timezone


class UrlyBirdBookmarksTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(

                                            username="UrlyBirdTest",
                                            email="urlybirdtest@test.com",
                                            password="password"
                                                                            )

        self.testbookmark = Bookmark.objects.create(

                                            url="www.test.com",
                                            title="this is atest",
                                            description="Testing my UrlyBird",
                                            user=self.user
                                                                            )

        self.testclick = self.testbookmark.click_set.create(
                                            bookmark=self.testbookmark,
                                            user=self.user
                                                                            )

    def test_click_total(self):
        self.assertEqual(self.testbookmark.click_total, 1,
                         "click count incorrect")

    def test_month_clicks(self):
        self.assertEqual(self.testbookmark.month_clicks, 1,
                         "month click incorrect")

    def test_month_clicks_false(self):
        old_time = timezone.now() - datetime.timedelta(days=31)
        self.testclick.created_at = old_time
        self.testclick.save()

        self.assertFalse(self.testbookmark.month_clicks,
                         "month click incorrectly true")





