from django.core.management import BaseCommand
from django.db.models import Count

from bookmarksite.models import Bookmark
from django.utils import timezone

import datetime
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Write a csv file of bookmarks with the most clicks over the past
        two days, ranked highest to lowest.
        """
        two_days_ago = timezone.now() - datetime.timedelta(days=2)
        results = Bookmark.objects.filter(
            click__created_at__gte=two_days_ago).annotate(
            num_count=Count("click")).order_by("-num_count")
        with open("top_marks.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Bookmark', 'Clicks'])
            for bookmark in results:
                writer.writerow([bookmark.title, bookmark.click_count])
