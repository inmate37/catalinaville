from typing import (
    Optional,
)
from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)
from django.views import View
# from django.views.generic.base import TemplateView

from abstracts.handlers import ViewHandler
from auths.forms import CustomUserForm
from auths.models import CustomUser
from university.models import Homework
from university.forms import HomeworkForm


class IndexView(ViewHandler, View):
    """Index View."""

    queryset: QuerySet = Homework.objects.get_not_deleted()
    template_name: str = 'university/index.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler."""

        response: Optional[HttpResponse] = \
            self.get_validated_response(
                request
            )
        if response:
            return response

        homeworks: QuerySet = self.queryset.filter(
            user=request.user
        )
        if not homeworks:
            homeworks = self.queryset

        context: dict = {
            'ctx_title': 'Главная страница',
            'ctx_homeworks': homeworks,
        }
        return self.get_http_response(
            request,
            self.template_name,
            context
        )


class CreateHomeworkView(ViewHandler, View):
    """CreateHomework View."""

    form: HomeworkForm = HomeworkForm

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler."""

        response: Optional[HttpResponse] = \
            self.get_validated_response(
                request
            )
        if response:
            return response

        return self.get_http_response(
            request,
            'university/homework_create.html',
            {'ctx_form': self.form()}
        )

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """POST request handler."""

        from django.shortcuts import redirect

        _form: HomeworkForm = self.form(
            request.POST or None,
            request.FILES or None
        )
        if not _form.is_valid():
            return self.get_http_response(
                request,
                'university/homework_create.html',
                {'ctx_form': _form}
            )
        homework = _form.save(commit=False)
        homework.user = request.user
        homework.logo = request.FILES['logo']

        file_type: str = homework.logo.url.split('.')[-1].lower()

        if file_type not in Homework.IMAGE_FILE_TYPES:
            context: dict = {
                'ctx_form': _form,
                'ctx_homework': homework,
                'error_message': 'PNG, JPG, JPEG'
            }
            return self.get_http_response(
                request,
                'university/homework_create.html',
                context
            )
        return redirect('page_main')
        return self.get_http_response(
            request,
            'university/index.html'
        )


class ShowView(ViewHandler, View):
    """Show View."""

    queryset: QuerySet = Homework.objects.get_not_deleted()
    template_name: str = 'university/profile.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler."""

        homework_id: int = kwargs.get(
            'homework_id', 0
        )
        homework: Optional[CustomUser] = None
        try:
            homework = self.queryset.filter(
                user=request.user
            ).get(
                id=homework_id
            )
        except Homework.DoesNotExist:
            return self.get_http_response(
                request,
                'university/index.html'
            )
        else:
            context: dict = {
                'ctx_title': 'Профиль пользователя',
                'ctx_homework': homework,
            }
            return self.get_http_response(
                request,
                self.template_name,
                context
            )


class DeleteView(ViewHandler, View):
    """Delete View."""

    def post(request: WSGIRequest) -> HttpResponse:
        """POST request handler."""
        pass


def about(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        template_name='university/about.html'
    )


def primitive(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Примитивная страница</h1>'
    )


class LoginView(ViewHandler, View):
    """Login View."""

    template_name: str = 'university/login.html'
def logout(request: WSGIRequest) -> HttpResponse:

    dj_logout(request)

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    context: dict = {
        'ctx_form': form,
    }
    return render(
        request,
        'university/login.html',
        context
    )


class LoginView(ViewHandler, View):
    """Login View."""

    template_name: str = 'university/login.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler."""

        return self.get_http_response(
            request,
            self.template_name
        )

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """POST request handler."""

        email: str = request.POST['username']
        password: str = request.POST['password']

        user: CustomUser = dj_authenticate(
            username=email,
            password=password
        )
        if not user:
            return self.get_http_response(
                request,
                self.template_name,
                {'error_message': 'Неверные данные'}
            )
        if not user.is_active:
            return self.get_http_response(
                request,
                self.template_name,
                {'error_message': 'Ваш аккаунт был удален'}
            )
        dj_login(request, user)

        homeworks: QuerySet = \
            Homework.objects.get_not_deleted().filter(
                user=request.user
            )
        context: dict = {
            'ctx_title': 'Домашние работы',
            'ctx_homeworks': homeworks
        }
        return self.get_http_response(
            request,
            'university/index.html',
            context
        )


class RegisterView(ViewHandler, View):
    """Register View."""

    template_name: str = 'university/register.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler."""

        return self.get_http_response(
            request,
            self.template_name
        )

    def post(request: WSGIRequest) -> HttpResponse:
        """POST request handler."""

        form: CustomUserForm = CustomUserForm(
            request.POST
        )
        if not form.is_valid():
            return render(
                request,
                'university/register.html',
                {'ctx_form': form}
            )
        user: CustomUser = form.save(
            commit=False
        )
        email: str = form.cleaned_data['email']
        password: str = form.cleaned_data['password']
        user.email = email
        user.set_password(password)
        user.save()

        user: CustomUser = dj_authenticate(
            email=email,
            password=password
        )
        if user and user.is_active:

            dj_login(request, user)

            homeworks: QuerySet = Homework.objects.filter(
                user=request.user
            )
            return self.get_http_response(
                request,
                'university/index.html',
                {'ctx_homeworks': homeworks}
            )
