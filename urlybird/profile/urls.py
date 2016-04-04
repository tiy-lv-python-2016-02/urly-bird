from django.conf.urls import url
from profile.views import ProfileBookmarkList, PublicProfileBookmarkList, \
    UserList
from urlsandbookmarks.views import UrlyLink

urlpatterns = [
    url(r'^dashboard/$', ProfileBookmarkList.as_view(), name="dashboard"),
    url(r'^profile/(?P<pk>\d+)/$', PublicProfileBookmarkList.as_view(),
        name="public_profile"),
    url(r'^users/$', UserList.as_view(), name="user_list"),
]
