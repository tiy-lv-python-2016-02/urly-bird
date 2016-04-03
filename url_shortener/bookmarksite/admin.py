from django.contrib import admin

from bookmarksite.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "url")



















