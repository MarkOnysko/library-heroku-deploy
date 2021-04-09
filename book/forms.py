from django import forms
from .models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']
        widgets = {
            'authors': forms.CheckboxSelectMultiple()
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) == 0:
            raise forms.ValidationError('Name must be filled')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) == 0:
            raise forms.ValidationError('Description must be filled')
        return description

    def clean_count(self):
        count = self.cleaned_data.get('count')
        if count < 0:
            raise forms.ValidationError('Count must be positive')
        return count

    # def clean_authors(self):
    #     authors = self.cleaned_data.get('authors')
    #     if authors is None:
    #         raise forms.ValidationError('You must select author')
    #     return authors