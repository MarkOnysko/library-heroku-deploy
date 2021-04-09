from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) == 0:
            raise forms.ValidationError('Name must be filled')
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if len(surname) == 0:
            raise forms.ValidationError('Surname must be filled')
        return surname