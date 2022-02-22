from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('show', views.show),
    # path('about/', views.about),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     path('', views.index_3, name='page_home'),
#     path('about/', views.about, name='page_about'),
#     path('index_2', views.index_2, name='page_index_2'),
# ]
