from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index_2', views.index_2),
    path('index_3', views.index_3),
    path('show', views.show),
    #path('about/', views.about),
]
