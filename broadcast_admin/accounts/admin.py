from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Team

class TeamAdmin(admin.ModelAdmin):
    model = Team
    fields = ['team_name', 'team_deps']

class TeamInline(admin.TabularInline):
    model = Team

class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['name', 'level', 'team']
    fields = ['username', 'name', 'level', 'team', 'number', 'phone', 'birth', 'email']
    inline = [
        TeamInline,
        ]

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Team, TeamAdmin)
