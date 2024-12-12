from django.contrib import admin

from Petstagram.pets.models import Pets


# Register your models here.
@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    readonly_fields = ('slug',)
