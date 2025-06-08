from django.contrib import admin

from places.models import Image, Place


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    pass

@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    pass