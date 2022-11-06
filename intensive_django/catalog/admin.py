from django.contrib import admin
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from .models import Item, Tag, Category, MainImage, GalleryImage


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'img_thumb')
    list_editable = ('is_published', )
    list_display_links = ('name', )
    filter_horizontal = ('tags', )

    def get_img(self, obj):
        return get_thumbnail(obj.mainimage.image, "300x300", crop='center',
                             qualify=51)

    def img_thumb(self, obj):
        if obj.mainimage.item:
            return mark_safe(f'<img src="{self.get_img(obj).url}">')
        return "Нет изображения"

    img_thumb.short_description = 'Превью'
    img_thumb.allow_tags = True


admin.site.register(Tag)
admin.site.register(Category)


@admin.register(MainImage)
class AdminMainImage(admin.ModelAdmin):
    list_display = ('img_name', 'img_thumb',)

    def get_img(self, obj):
        return get_thumbnail(obj.image, "300x300", crop='center',
                             qualify=51)

    def img_thumb(self, obj):
        if obj.item:
            return mark_safe(f'<img src="{self.get_img(obj).url}">')
        return "Нет изображения"

    def img_name(self, obj):
        return obj.item.name

    img_thumb.short_description = 'Превью'
    img_thumb.allow_tags = True


@admin.register(GalleryImage)
class AdminGalleryImage(admin.ModelAdmin):
    list_display = ('img_name', 'img_thumb',)

    def get_img(self, obj):
        return get_thumbnail(obj.image, "300x300", crop='center',
                             qualify=51)

    def img_thumb(self, obj):
        if obj.item:
            return mark_safe(f'<img src="{self.get_img(obj).url}">')
        return "Нет изображения"

    def img_name(self, obj):
        return obj.item.name

    img_thumb.short_description = 'Превью'
    img_thumb.allow_tags = True
