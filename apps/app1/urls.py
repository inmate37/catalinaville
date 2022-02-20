from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('show', views.show),
    # path('about/', views.about),
]
# urlpatterns = [
#     path('', views.index_3, name='page_home'),
#     path('about/', views.about, name='page_about'),
#     path('index_2', views.index_2, name='page_index_2'),
# ]
