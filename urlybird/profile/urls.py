from django.conf.urls import url
from profile.views import ProfileBookmarkList, PublicProfileBookmarkList, \
    UserList, ProfileUpdate, StatsView
from urlsandbookmarks.views import UrlyLink

urlpatterns = [
    url(r'^dashboard/$', ProfileBookmarkList.as_view(), name="dashboard"),
    url(r'^profile/(?P<profile_id>\d+)/$', PublicProfileBookmarkList.as_view(),
        name="public_profile"),
    url(r'^users/$', UserList.as_view(), name="user_list"),
    url(r'^profile/update/(?P<pk>\d+)/$', ProfileUpdate.as_view(),
        name="profile_update"),
    url(r'^click_stats/$', StatsView.as_view(), name="click_stats"),

]
