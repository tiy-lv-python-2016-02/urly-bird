from django import forms
from django.forms import Textarea
from urlsandbookmarks.models import Bookmark


class BookmarkForm(forms.ModelForm):

    class Meta:

        model = Bookmark

        fields = ('url', 'title', 'description')
        widgets = {
            'description': Textarea(attrs={'rows':4, 'cols': 45})
        }
