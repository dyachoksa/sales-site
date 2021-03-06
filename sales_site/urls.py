"""sales_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages.views import flatpage
from django.urls import path, re_path, include

from blog.views import BlogIndexView
from pages.views import HomePage, OurTeamView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path("blog/", BlogIndexView.as_view(), name="blog_index"),
    path("our-team/", OurTeamView.as_view(), name="our-team"),
    path("", HomePage.as_view(), name="home"),
    re_path(r"^(?P<url>.*/)$", flatpage),
    prefix_default_language=False,
)

if settings.DEBUG:
    import debug_toolbar  # noqa

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
