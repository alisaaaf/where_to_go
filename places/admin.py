from django.contrib import admin

from places.models import Image, Place

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [ImageInline]

@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    pass