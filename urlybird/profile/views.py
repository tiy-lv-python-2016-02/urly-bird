from urlsandbookmarks.forms import BookmarkForm
from urlsandbookmarks.models import Bookmark
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, \
    UpdateView, DeleteView


class ProfileBookmarkList(LoginRequiredMixin, ListView):

    model = Bookmark
    paginate_by = 10
    template_name = "profile/dashboard.html"

    def get_queryset(self):
        query = Bookmark.objects.all().filter(user=self.request.user)\
            .order_by('-created_at')
        return query


class PublicProfileBookmarkList(DetailView):
    model = User
    template_name = "profile/public_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmarks"] = self.object.bookmark_set.all()
        return context


class UserList(ListView):

    model = User
    paginate_by = 10
    template_name = "profile/user_list.html"


class RegisterUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("bookmark_list")



class BookmarkUpdate(LoginRequiredMixin, UpdateView):
    """
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
    model = Bookmark
    success_url = reverse_lazy('bookmark_list')
    template_name = 'urlsandbookmarks/bookmark_delete.html'
