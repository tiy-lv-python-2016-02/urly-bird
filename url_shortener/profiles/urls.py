from django.conf.urls import url

from bookmarksite.views import UserList, UserDetail


urlpatterns = [
    url(r'^$', UserList.as_view(), name="user_list"),
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view(), name="user_detail"),
]
