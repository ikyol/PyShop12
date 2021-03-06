from django import forms
from django.contrib.auth.models import User

from account.utils import send_welcome_email


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(min_length=8, required=True,
                               widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True,
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already used')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This email is already used')
        return username

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError('Дурак у тебя пароли не совпадают ты тупая мозга')
        return data

    def save(self, commit=True):
        from .utils import send_mail
        user = User.objects.create_user(**self.cleaned_data)
        send_welcome_email(user.email)
        return user