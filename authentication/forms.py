from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', "last_name", 'email', 'password1', 'password2')



class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=150,
                               label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=150,
                                label='Confirm password',
                                widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', "last_name")


class UsersChangePermissionsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("role", "is_active")
