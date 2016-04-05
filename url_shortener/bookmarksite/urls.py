from django.conf.urls import url

from bookmarksite.views import BookmarkDetail, BookmarkCreate, BookmarkList,\
    BookmarkUpdate, BookmarkDelete


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BookmarkDetail.as_view(), name="bookmark_detail"),
    url(r'^create$', BookmarkCreate.as_view(), name="bookmark_create"),
    url(r'^$', BookmarkList.as_view(), name="bookmark_list"),
    url(r'^update/(?P<id>\d+)/$', BookmarkUpdate.as_view(),
        name="bookmark_update"),
    url(r'^delete/(?P<pk>\d+)/$', BookmarkDelete.as_view(),
        name="bookmark_delete"),
]
