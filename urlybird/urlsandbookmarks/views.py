from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, RedirectView
from hashids import Hashids
from urlsandbookmarks.forms import BookmarkForm
from urlsandbookmarks.models import Bookmark, Click
import pickle


class BookmarkDetail(DetailView):
    """
    uses Bookmark model
    get_context_data is overwritten
    to add session data with which links
    were visited by bookmark.id & bookmark.title
    each visit is kept in a dictionary appended
    visitor_list list
    the overall list is sliced to only give last 5
    """

    model = Bookmark

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        visitor_list = self.request.session.get("visitor_list", [])
        visitor_list.append({self.object.id: self.object.title})

        self.request.session["visitor_list"] = visitor_list[-5:]

    # list to store title
        # list of dictionaries
        return context


class BookmarkList(ListView):
    """
    ListView of the Bookmark model
    queryset is set to all bookmark objects
    ordered by last created ('-created_at')
    pagination set to 5
    """

    model = Bookmark
    paginate_by = 5
    queryset = Bookmark.objects.order_by("-created_at")


class BookmarkCreate(LoginRequiredMixin, CreateView):
    """
    LoginRequired to access
    CreateView for the
    Bookmark model
    form_class BookmarkForm
    returns user to the main bookmark_list after completion
    template name "bookmark_create"
    """

    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy("bookmark_list")
    template_name_suffix = "_create"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UrlyLink(RedirectView):
    """
    RedirectView to make the urlybird link work
    decodes hash id to get matching bookmark
    creates click object with user if user logged in
    if not creates click object with null user
    click objects also have the bookmark object attached
    """
    pattern_name = "urly_redirect"

    def get_redirect_url(self, *args, **kwargs):
        hash_id = Hashids()
        hashed = kwargs['hash_id']
        decoded = hash_id.decode(hashed)
        bookmark = get_object_or_404(Bookmark, id=decoded[0])
        if self.request.user in User.objects.all():
            Click.objects.create(bookmark=bookmark, user=self.request.user)
        else:
            Click.objects.create(bookmark=bookmark)
        return bookmark.url
