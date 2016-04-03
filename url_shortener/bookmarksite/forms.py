from django import forms
from bookmarksite.models import Bookmark


class BookmarkForm(forms.ModelForm):

    class Meta:
        model = Bookmark
        fields = ("title", "description", "url")









