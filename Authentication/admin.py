from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import TextInput, Textarea, CharField
from django import forms

from Authentication.models import MyUser

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = MyUser
    search_fields = ('email', 'user_name', 'first_name')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)})
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})}
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active')
        })
    )

admin.site.register(MyUser, UserAdminConfig)