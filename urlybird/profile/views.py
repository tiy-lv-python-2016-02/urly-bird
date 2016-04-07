from django.db.models import Count
from django.shortcuts import get_object_or_404
from profile.forms import ProfileForm
from profile.models import Profile
from urlsandbookmarks.forms import BookmarkForm
from urlsandbookmarks.models import Bookmark
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, \
    UpdateView, DeleteView


class ProfileBookmarkList(LoginRequiredMixin, ListView):
    """
    ListView for the dashboard page
    This page is for the user logged in only
    Bookmark model
    pagination set to 5
    template name profile/dashboard.html

    get_queryset has been overridden
    to get all bookmark objects from logged in user
    ordered by last created (-created_at)
    """

    model = Bookmark
    paginate_by = 5
    template_name = "profile/dashboard.html"

    def get_queryset(self):
        query = Bookmark.objects.all().filter(user=self.request.user)\
            .order_by('-created_at')
        return query


class PublicProfileBookmarkList(ListView):
    """
    ListView for the public profile
    Using the Bookmark model
    Only gets Bookmarks from that user
    could later be improved
    get the user as well to use more of their
    data on that page
    pagination set to 5
    template_name profile/public_profile.html
    """
    model = Bookmark
    template_name = "profile/public_profile.html"
    paginate_by = 5

    def get_queryset(self):
        user_profile = get_object_or_404(User, profile=self.kwargs['profile_id'])
        return Bookmark.objects.all().filter(user__profile=user_profile.profile.id)


class UserList(ListView):
    """
    ListView to display all the Users
    pagination at 10
    template name profile/user_list.html
    """

    model = User
    paginate_by = 10
    template_name = "profile/user_list.html"


class RegisterUser(CreateView):
    """
    CreateView for registering a User
    uses the Django UserCreationForm
    template name registration/register.html
    upon completion user sent to bookmark_list
    """
    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("bookmark_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response


class BookmarkUpdate(LoginRequiredMixin, UpdateView):
    """
    UpdateView for Bookmark model
    Login required
    option to update bookmark's url, title, description
    uses BookmarkForm for form_class
    successful update form will return user to the details
    of that bookmark by id
    """

    model = Bookmark
    form_class = BookmarkForm

    template_name = "urlsandbookmarks/bookmark_update.html"

    def get_success_url(self):
        return reverse('bookmark_detail', args=(self.object.id,))


class BookmarkDelete(LoginRequiredMixin, DeleteView):
    """
    DeleteView for Bookmark model
    Login Required
    returns user to bookmark_list upon successful deletion
    template name: urlsandbookmarks/bookmark_delete.html
    """

    model = Bookmark
    success_url = reverse_lazy('bookmark_list')
    template_name = 'urlsandbookmarks/bookmark_delete.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    """
    UpdateView for Profile model
    Login Required
    form class used is ProfileForm (found in profile/forms.py)
    template name profile/profile_update.html
    returns user to dashboard upon successful update
    Image is available to to upload on this form
    """

    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('dashboard')
    template_name = "profile/profile_update.html"

    def form_valid(self, form):
        return super().form_valid(form)


class StatsView(LoginRequiredMixin, ListView):
    """
    Click Stats page
    ListView for Bookmark model
    Login Required
    pagination set to 10
    template name profile/click_stats.html
    get_queryset gets all bookmarks by logged in user
    and gets a total count of clicks on their bookmark link
    ordered by the total click
    """

    model = Bookmark
    paginate_by = 10
    template_name = "profile/click_stats.html"

    def get_queryset(self):
        query = Bookmark.objects.all().filter(user=self.request.user) \
            .annotate(total_clicks=Count('click')).order_by('-total_clicks')
        return query

