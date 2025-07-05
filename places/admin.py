from adminsortable2.admin import SortableAdminBase
from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Image, Place


class ImageInline(SortableAdminBase, admin.TabularInline):
    model = Image
    extra = 1

    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" style="max-height: 200px;" />'.format(
                url=obj.image.url
            ))
        return "(Изображение не загружено)"


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [ImageInline]

@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    raw_id_fields = ("place",)

