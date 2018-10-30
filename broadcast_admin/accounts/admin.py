from django.contrib import admin
from .models import CustomUser, Team

admin.site.register(Team)

class TeamInline(admin.TabularInline):
    model = Team

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'name', 'level', 'team', 'number', 'phone', 'birth', 'email']
    inline = [
        TeamInline,
        ]

admin.site.register(CustomUser, UserAdmin)
