from django.urls import (
    path,
    re_path,
)
from university import views
from university.views import (
    IndexView,
    ShowView,
    LoginView,
    RegisterView,
    DeleteView,
    CreateHomeworkView,
)


urlpatterns = [
    path('',                        IndexView.as_view(), name='page_main'),
    path('show/<int:homework_id>/', ShowView.as_view(),  name='page_show'),
    path('delete/',                 DeleteView.as_view(), name='page_delete'),
    path('about/',                  views.about,         name='page_about'),
    path('primitive/',              views.primitive,     name='page_primitive'),  # noqa

    path('register/', RegisterView.as_view(), name='page_register'),
    path('login/',    LoginView.as_view(), name='page_login'),
    path('logout/',   views.logout,   name='page_logout'),

    path(
        'create_homework/',
        CreateHomeworkView.as_view(),
        name='page_create_homework'
    ),
    path(
        'homework_create/',
        CreateHomeworkView.as_view(),
        name='page_homework_create'
    ),
]
