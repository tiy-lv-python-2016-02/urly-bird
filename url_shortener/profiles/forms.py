from django import forms
from django.contrib.auth.models import User

from profiles.models import Profile


class ImageUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("image",)
