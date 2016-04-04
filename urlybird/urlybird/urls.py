"""urlybird URL Configuration

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
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy
from profile.views import RegisterUser
from urlsandbookmarks.views import UrlyLink

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("profile.urls")),
    url(r'^', include("urlsandbookmarks.urls")),
    url(r'^b/(?P<hash_id>\w+)/$', UrlyLink.as_view(),
        name="urly_redirect"),
    url(r'^logout/$', logout, {'next_page': reverse_lazy('bookmark_list')},
        name='logout'),
    url(r'^register/$', RegisterUser.as_view(), name="register"),
    url('^', include('django.contrib.auth.urls'))
]
