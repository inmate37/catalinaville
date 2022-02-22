from django.urls import path
from . import views


urlpatterns = [
    path('',           views.index,     name='page_main'),
    path('show/',      views.show,      name='page_show'),
    path('about/',     views.about,     name='page_about'),
    path('primitive/', views.primitive, name='page_primitive')
]
