from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import (
    ValidationError,
)


class Group(models.Model):
    NAME_MAX_LENGTH = 10

    name = models.CharField(
        verbose_name='имя',
        max_length=NAME_MAX_LENGTH
    )

    def __str__(self) -> str:
        return f'Группа: {self.name}'

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Account(models.Model):
    FULL_NAME_MAX_LENGTH = 20

    user = models.OneToOneField(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        verbose_name='полное имя',
        max_length=FULL_NAME_MAX_LENGTH
    )
    description = models.TextField()

    def __str__(self) -> str:
        return f'Аккаунт: {self.user.id} / {self.full_name}'

    class Meta:
        ordering = (
            'full_name',
        )
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


class Student(models.Model):
    MAX_AGE = 27

    account = models.OneToOneField(
        Account,
        verbose_name='аккаунт',
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        verbose_name='группа',
        on_delete=models.PROTECT
    )
    age = models.IntegerField(
        verbose_name='Возраст студента',
    )
    gpa = models.FloatField(
        verbose_name='Среднее значение GPA'
    )

    def __str__(self) -> str:
        return 'Студент: {0} / {1} / {2}'.format(
            self.account.full_name,
            self.age,
            self.gpa,
        )

    def save(
        self,
        *args: tuple,
        **kwargs: dict
    ) -> None:
        if self.age > self.MAX_AGE:
            # v1
            #self.age = self.MAX_AGE

            # v2
            raise ValidationError(
                f'Допустимый возраст: {self.MAX_AGE}'
            )
        # if self.age <= self.MAX_AGE:
        #     pass

        super().save(*args, **kwargs)


    class Meta:
        ordering = (
            'gpa',
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
