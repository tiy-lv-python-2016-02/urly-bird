from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView

from profiles.models import Profile
from profiles.forms import ImageUpdateForm


class RegisterUser(CreateView):

    model = User

    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("bookmark_list")

    def form_valid(self, form):

        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ImageUpdateForm
    template_name = "registration/image_update.html"
    success_url = reverse_lazy("bookmark_list")
    pk_url_kwarg = "id"

    def form_valid(self, form):

        a='b'
        a='c'
        return super().form_valid(form)

