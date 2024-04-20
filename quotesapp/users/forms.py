from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput()
                               )

    email = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput())

    password1 = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.PasswordInput()
                                )

    password2 = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.PasswordInput()
                                )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        field = ['username', 'password']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    # Оновлення віджетів для встановлення CSS-класів
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
