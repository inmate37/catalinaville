from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from app1.models import Student


def index(request: WSGIRequest) -> HttpResponse:
    users: User = User.objects.all()

    return render(
        request,
        "index.html",
        context={"users":users}
    )


def show(request: WSGIRequest) -> HttpResponse:
    user: User = User.objects.first()
    name: str = user.first_name
    text: str = f'<h1>Имя: {name}</h1>'

    response: HttpResponse = HttpResponse(text)
    return response


def index_2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Страница: Стартовая</h1>'
    )


def index_3(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = User.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users': users,
    }
    # return render(
    #     request,
    #     'index.html',
    #     context
    # )
    return render(
        request,
        "index_2.html",
        context={"users":1}
    )


# def index_3(request: WSGIRequest) -> HttpResponse:
#     students = Student.objects.all()
#     context: dict = {
#         'title': 'Главная страница',
#         'students': students
#     }
#     return render(
#         request,
#         'index.html',
#         context
#     )


# def about(request: WSGIRequest) -> HttpResponse:
#     return render(request, 'about.html')
