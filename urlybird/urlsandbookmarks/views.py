from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, RedirectView
from urlsandbookmarks.forms import BookmarkForm
from urlsandbookmarks.models import Bookmark, Click


class BookmarkDetail(DetailView):

    model = Bookmark


class BookmarkList(ListView):

    model = Bookmark
    paginate_by = 20
    queryset = Bookmark.objects.order_by("-created_at")


class BookmarkCreate(LoginRequiredMixin, CreateView):

    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy("bookmark_list")
    template_name_suffix = "_create"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UrlyLink(RedirectView):
    pattern_name = "urly_redirect"

    def get_redirect_url(self, *args, **kwargs):
        bookmark = get_object_or_404(Bookmark, pk=kwargs['pk'])
        Click.objects.create(bookmark=bookmark)
        return bookmark.url

    # work in progress