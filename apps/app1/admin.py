from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin

from app1.models import (
    Account,
    Student,
    Group,
)


class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ()

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if not obj:
            return self.readonly_fields
        return self.readonly_fields + ('description',)


class StudentAdmin(admin.ModelAdmin):
    STUDENT_EDIT_MAX_AGE = 16

    readonly_fields = ()

    def student_age_validation(
        self,
        obj: Optional[Student]
    ) -> tuple:
        if obj and obj.age <= self.STUDENT_EDIT_MAX_AGE:
            return self.readonly_fields + ('age',)
        return self.readonly_fields

    def student_age_validation_2(
        self,
        obj: Optional[Student]
    ) -> bool:
        if obj and obj.age <= self.STUDENT_EDIT_MAX_AGE:
            return True
        return False

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Student] = None
    ) -> tuple:

        # v1 | student_age_validation
        #
        result: tuple = self.student_age_validation(obj)
        return result

        # v2 | student_age_validation_2
        #
        # result: bool = self.student_age_validation_2(obj)
        # if result:
        #     return self.readonly_fields + ('age',)
        # return self.readonly_fields


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ()


admin.site.register(
    Account, AccountAdmin
)
admin.site.register(
    Group, GroupAdmin
)
admin.site.register(
    Student, StudentAdmin
)



























class StudentAdmin(admin.ModelAdmin):
    STUDENT_EDIT_MAX_AGE = 16

    readonly_fields = ()
    list_display = ('get_account_full_name', 'age', 'gpa',)
    list_filter = ('age',)
    search_fields = ('age',)

    def get_account_full_name(self, obj):
        return obj.account.full_name

    get_account_full_name.short_description = 'Аккаунт'
    get_account_full_name.admin_order_field = 'account__full_name'

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        age_condition: bool = obj.age <= self.STUDENT_EDIT_MAX_AGE

        if obj and age_condition:
            return self.readonly_fields + ('age',)

        return self.readonly_fields


        age_condition: bool = obj.age <= self.STUDENT_EDIT_MAX_AGE
        if obj and age_condition:
            return self.readonly_fields + ('age',)