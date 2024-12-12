from django.contrib import admin

from Artonia.products.models import Macrame, ArtPainting


# Register your models here.

@admin.register(Macrame)
class MacrameAdmin(admin.ModelAdmin):
    pass


@admin.register(ArtPainting)
class ArtPainingAdmin(admin.ModelAdmin):
    pass
