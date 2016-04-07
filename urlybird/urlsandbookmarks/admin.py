from django.contrib import admin
from urlsandbookmarks.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'title', 'description', 'created_at',
                    'user', 'modified_at')
