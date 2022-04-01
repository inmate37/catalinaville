from django import forms

from university.models import Homework


class HomeworkForm(forms.ModelForm):

    class Meta:
        model = Homework
        fields = (
            'title',
            'subject',
            'logo',
        )
