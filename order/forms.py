from django import forms
from .models import *


class CreateOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].empty_label = 'Please select a user'
        self.fields['book'].empty_label = 'Please select a book'

    class Meta:
        model = Order
        fields = ['user', 'book']

    def clean_book(self):
        book = self.cleaned_data.get('book')
        if book.count <= 1:
            raise forms.ValidationError('There is the last book in our library. Please try to order it later')
        return book


class UpdateOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['end_at', 'plated_end_at']
        widgets = {
            'end_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'plated_end_at': forms.DateTimeInput()
        }