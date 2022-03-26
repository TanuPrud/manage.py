from django.forms import ModelForm, TextInput, Textarea

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title","task")
        widgest = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholdor': 'Введите название'
        }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholdor': 'Введите описание'
            }),
        }