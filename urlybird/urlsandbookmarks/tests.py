from django.test import TestCase

import datetime
from django.test import TestCase
from urlsandbookmarks.models import Bookmark, Click
from django.contrib.auth.models import User
from django.utils import timezone


class UrlyBirdBookmarksTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user\
                                            (
                                            username="UrlyBirdTest",
                                            email="urlybirdtest@test.com",
                                            password="password"
                                                                            )

        self.testbookmark = Bookmark.objects.create\
                                            (
                                            description="Testing my UrlyBirdBookmark",
                                            name="TestUrly"
                                                                            )
        self.testclick = Click.objects.create



    def test_today_count(self):
        self.assertEqual(self.testbookmark.today_count)





