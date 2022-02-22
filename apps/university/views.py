from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from university.models import Student


def index(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = User.objects.all()
    context: dict = {
        'title': 'Главная страница',
        'users': users,
    }
    return render(
        request,
        template_name='university/index.html',
        context=context
    )


def show(request: WSGIRequest) -> HttpResponse:
    user: User = User.objects.first()
    name: str = user.first_name
    text: str = f'<h1>Имя: {name}</h1>'

    response: HttpResponse = HttpResponse(text)
    return response


def about(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        template_name='university/about.html'
    )


def index_2(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = User.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users': users,
    }
    return render(
        request,
        template_name='university/index_2.html',
        context=context
    )


def index_3(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Главная страница III</h1>'
    )
