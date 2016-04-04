from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, ListView, UpdateView,\
    DeleteView, RedirectView

from bookmarksite.models import Bookmark, Click
from bookmarksite.forms import BookmarkForm
from hashids import Hashids

import datetime

from django.utils import timezone
from django.db.models import Count


class BookmarkList(ListView):
    model = Bookmark
    queryset = Bookmark.objects.order_by("-modified_at")
    template_name = "bookmarksite/bookmark_list.html"
    context_object_name = "bookmarks"
    paginate_by = 5


class BookmarkDetail(DetailView):
    model = Bookmark
    template_name = "bookmarksite/bookmark_detail.html"
    context_object_name = "bookmark"


class BookmarkCreate(LoginRequiredMixin, CreateView):
    model = Bookmark
    form_class = BookmarkForm

    success_url = reverse_lazy("bookmark_list")
    template_name = "bookmarksite/bookmark_create.html"
    pk_url_kwarg = "id"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookmarkUpdate(UpdateView):
    model = Bookmark
    form_class = BookmarkForm
    template_name = "bookmarksite/bookmark_update.html"
    pk_url_kwarg = "id"

    def get_success_url(self):
        return reverse("bookmark_list")


class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name = "bookmarksite/bookmark_delete.html"
    success_url = reverse_lazy("bookmark_list")


class RerouteLink(RedirectView):
    permanent = False
    pattern_name = "view_reroute"

    def get_redirect_url(self, *args, **kwargs):
        """
        The redirect url is constructed with a reversible hash of the
        bookmark's id.
        id_num reverses that hash.
        :return: The url of the bookmark that is gotten with the id_num.
        """
        hashid = Hashids()
        hash_val = self.kwargs["hash_id"]
        id_num = hashid.decode(hash_val)[0]
        bookmark = get_object_or_404(Bookmark, pk=id_num)
        if self.request.user is User:
            Click.objects.create(bookmark=bookmark, user=self.request.user)
        else:
            Click.objects.create(bookmark=bookmark)
        return bookmark.url


class UserList(ListView):
    queryset = User.objects.all()
    template_name = "bookmarksite/user_list.html"
    context_object_name = "users"


class UserDetail(ListView):
    template_name = "bookmarksite/user_detail.html"
    context_object_name = "bookmarks"
    paginate_by = 5

    def get_queryset(self):
        """
        Filters bookmarks to those of the user displayed on the page. Sorted
        with the most recent first.
        """
        profiled_user = User.objects.get(pk=self.kwargs['pk'])
        return Bookmark.objects.filter(
            user=profiled_user).order_by("-created_at")

    def get_context_data(self, **kwargs):
        """
        user_match is True if the user displayed on the page is the same
        user that is visiting the page. This enables the delete/edit options.
        """
        context = super().get_context_data(**kwargs)
        profiled_user = User.objects.get(pk=self.kwargs['pk'])
        context["profiled_user"] = profiled_user
        context["user_match"] = self.request.user == profiled_user
        return context


class UserStats(DetailView):
    model = User
    template_name = "bookmarksite/user_stats.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        """
        Bookmark are sorted by the number of clicks from the past 30 days.
        """
        context = super().get_context_data(**kwargs)
        one_month_ago = timezone.now() - datetime.timedelta(days=30)

        context["bookmarks"] = self.object.bookmark_set.filter(
            click__created_at__gt=one_month_ago).annotate(
            num_count=Count('click')).order_by('-num_count')
        return context
