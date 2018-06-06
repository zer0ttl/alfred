from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'birth_year')


class CustomUserChangeForm(UserChangeForm):

    class Meta():
        model = CustomUser
        fields = UserChangeForm.Meta.fields