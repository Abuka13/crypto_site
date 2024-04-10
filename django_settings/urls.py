from django.conf import settings
from django.conf.urls import i18n
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_app.urls")),
    path("i18n/", include("django.conf.urls.i18n")),

]

