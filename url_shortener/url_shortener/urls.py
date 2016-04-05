"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import logout
from django.conf.urls.static import static
from django.conf import settings

from bookmarksite.views import RerouteLink
from profiles.views import RegisterUser, UpdateProfile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^b/(?P<hash_id>\w+)/$', RerouteLink.as_view(),
        name="view_reroute"),
    url(r'^bookmarks/', include("bookmarksite.urls")),
    url(r'^logout/$', logout, {'next_page': reverse_lazy("bookmark_list")},
        name='logout'),
    url(r'^register/$', RegisterUser.as_view(), name="register"),
    url(r'^users/update/(?P<id>\d+)/$', UpdateProfile.as_view(),
        name="update_profile"),
    url(r'^users/', include("profiles.urls")),
    url('^', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
