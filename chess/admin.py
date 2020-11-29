from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class ReviewInline(admin.TabularInline):
    """Отзывы на статью"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")

class ArticlesShotsInline(admin.TabularInline):
    model = ArticlesShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"

class ArticlesAdmin(admin.ModelAdmin):
    """Статьи"""
    list_display = ("title", "date_pub", "slug")
    search_fields = ("title", "intro_text", "full_text")
    inlines = [ArticlesShotsInline, ReviewInline]


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Treners)
admin.site.register(Files)
admin.site.register(Videos)
admin.site.register(Reviews)
admin.site.register(Index)
admin.site.register(Trenings)
admin.site.register(ArticlesShots)