from django.contrib import admin

from Artonia_v2.accounts.models import ArtoniaUser


@admin.register(ArtoniaUser)
class UserRegisterViewAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


