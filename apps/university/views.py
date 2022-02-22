from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from university.models import Student


def index(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = User.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users': users,
    }
    return render(
        request,
        template_name='university/index.html',
        context=context
    )


def show(request: WSGIRequest) -> HttpResponse:
    user: User = request.user

    # TODO: pass selected user ctx to template

    context: dict = {
        'ctx_title': 'Профиль пользователя',
        'ctx_user': user,
    }
    return render(
        request,
        template_name='university/profile.html',
        context=context
    )


def delete(request: WSGIRequest) -> HttpResponse:
    # TODO
    ...


def about(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        template_name='university/about.html'
    )


def primitive(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Примитивная страница</h1>'
    )
