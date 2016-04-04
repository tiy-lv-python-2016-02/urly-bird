from django.conf.urls import url
from profile.views import BookmarkUpdate, BookmarkDelete
from urlsandbookmarks.views import BookmarkDetail, BookmarkList, BookmarkCreate


urlpatterns = [
    url(r'^bookmark/detail/(?P<pk>\d+)/$', BookmarkDetail.as_view(),
        name="bookmark_detail"),
    url(r'^bookmark/update/(?P<pk>\d+)/$', BookmarkUpdate.as_view(),
        name="bookmark_update"),
    url(r'^bookmark/delete/(?P<pk>\d+)/$', BookmarkDelete.as_view(),
        name="bookmark_delete"),
    url(r'^$', BookmarkList.as_view(), name="bookmark_list"),
    url(r'^newbookmark/$', BookmarkCreate.as_view(), name="bookmark_create"),


]