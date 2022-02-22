from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(
        settings.ADMIN_SITE_URL,
        admin.site.urls
    ),
    path(
        '',
        include('app1.urls')
    ),
    path(
        '__debug__/',
        include('debug_toolbar.urls')
    ),
]
