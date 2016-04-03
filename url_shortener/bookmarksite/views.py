from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, ListView, UpdateView,\
    DeleteView, RedirectView

from bookmarksite.models import Bookmark, Click
from bookmarksite.forms import BookmarkForm
from profiles.models import Profile
from hashids import Hashids


class BookmarkList(ListView):
    model = Bookmark
    queryset = Bookmark.objects.order_by("-modified_at")
    template_name = "bookmarksite/bookmark_list.html"
    context_object_name = "bookmarks"
    paginate_by = 3


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
        Click.objects.create(bookmark=bookmark, user=self.request.user)
        return bookmark.url


class UserList(ListView):
    queryset = User.objects.all()
    template_name = "bookmarksite/user_list.html"
    context_object_name = "users"


class UserDetail(DetailView):
    model = User
    template_name = "bookmarksite/user_detail.html"
    context_object_name = "user"
    #paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmarks"] = self.object.bookmark_set.all()
        same_user = self.object == self.request.user
        context["user_match"] = same_user
        return context

