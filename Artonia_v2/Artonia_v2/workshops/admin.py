from django.contrib import admin

from Artonia_v2.workshops.models import Workshop


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'duration_hours', 'date', 'location')
    search_fields = ('title', 'instructor')
