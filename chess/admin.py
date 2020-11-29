from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class ReviewInline(admin.TabularInline):
    """Отзывы на статью"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class ArticleShotsInline(admin.TabularInline):
    model = ArticleShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    """Статьи"""
    list_display = ("title", "date_pub", "slug")
    search_fields = ("title", "intro_text", "full_text")
    inlines = [ArticleShotsInline, ReviewInline]
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title", "slug",),)
        }),
        (None, {
            "fields": ("intro_text", ("img", "get_image"))
        }),
        (None, {
            "fields": (("full_text",),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="100" height="110"')

    get_image.short_description = "Обложка статьи"


admin.site.register(Treners)
admin.site.register(Files)
admin.site.register(Videos)
admin.site.register(Reviews)
admin.site.register(Index)
admin.site.register(Trenings)
