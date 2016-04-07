from datetime import timedelta
import csv

from django.db.models import Count
from django.http import HttpResponse
from django.core.management import BaseCommand
from django.utils import timezone
from urlsandbookmarks.models import Bookmark


class Command(BaseCommand):
    """
    python manage.py archive_top_20
    saves the first 20 bookmarks ordered by the highest
    clicks
    """

    def handle(self, *args, **options):

        two_days_ago = timezone.now() - timedelta(days=2)
        qs = Bookmark.objects.filter(click__created_at__gte=two_days_ago).annotate(total_clicks=Count('click')).order_by('-total_clicks')


        self.stdout.write("Saving Top 20 Bookmarks to CSV File")

        with open("top_bookmarks.csv", 'w', newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Bookmark', 'Clicks in last Two Days'])
            for bookmark in qs:
                writer.writerow([bookmark.title, bookmark.click_total])

