import random
import names
from typing import Any
from datetime import datetime

from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import (
    User,
)
from django.contrib.auth.hashers import make_password

from university.models import (
    Group,
    Account,
    Student,
    Professor,
)


class Command(BaseCommand):
    """Custom command for filling up database.

    Test data only
    """
    help = 'Custom command for filling up database.'

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_number(self) -> int:
        """Generates number."""

        _number_from: int = 10
        _number_to: int = 99

        return random.randint(
            _number_from,
            _number_to
        )

    def _generate_users(self) -> None:
        """Generates User objects."""

        TOTAL_USERS_COUNT = 500

        def generate_username() -> str:
            return '{0}_{1}'.format(
                first_name.lower(),
                last_name.lower()
            )

        def generate_email() -> str:
            _email_patterns: tuple = (
                'gmail.com', 'outlook.com', 'yahoo.com',
                'inbox.ru', 'inbox.ua', 'inbox.kz',
                'yandex.ru', 'yandex.ua', 'yandex.kz',
                'mail.ru', 'mail.ua', 'mail.kz',
            )
            return '{0}.{1}@{2}'.format(
                first_name.lower(),
                last_name.lower(),
                random.choice(_email_patterns)
            )

        def generate_password() -> str:
            _passwd_pattern: str = 'abcde12345'
            _passwd_max_length: int = 8

            raw_password: str = ''.join(
                random.choice(_passwd_pattern)
                for _ in range(_passwd_max_length)
            )
            return make_password(raw_password)

        # Generating superuser
        #
        if not User.objects.filter(is_superuser=True).exists():
            superuser: dict = {
                'is_superuser': True,
                'username': 'dmytro',
                'email': 'dmytro@mail.ua',
                'password': 'barakobama',
                'first_name': 'Дмитрий',
                'last_name': 'Гордон',
            }
            User.objects.create_superuser(**superuser)

        # Generating users
        #
        if User.objects.filter(
            is_superuser=False
        ).count() == TOTAL_USERS_COUNT:
            return

        first_name: str = ''
        last_name: str = ''
        password: str = ''
        username: str = ''
        email: str = ''
        _: int
        for _ in range(TOTAL_USERS_COUNT):
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            username = generate_username()
            email = generate_email()
            password = generate_password()

            user: dict = {
                'username': username,
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
            }
            User.objects.get_or_create(**user)

    def _generate_groups(self) -> None:
        """Generates Group objs."""

        def generate_name(inc: int) -> str:
            return f'Группа {inc}'

        inc: int
        for inc in range(1, 21):
            name: str = generate_name(inc)
            Group.objects.create(
                name=name
            )

    def _generate_accounts_and_students(self) -> None:
        """Generates Account and Student objs."""
        pass

    def _generate_professors(self) -> None:
        """Generates Professor objs."""
        pass

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()

        self._generate_users()
        # self._generate_groups()
        # self._generate_accounts_and_students()
        # self._generate_professors()

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )
