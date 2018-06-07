from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'birth_year']
    search_fields = ['email', ]


admin.site.register(CustomUser, CustomUserAdmin)
