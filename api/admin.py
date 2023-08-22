from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)
    prepopulated_fields = {'slug': ('category_title',)}
@admin.register(Category)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)
    prepopulated_fields = {'slug': ('category_title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_title", "product_slug", "product_category", "product_price", "product_discount", "product_weight", "get_photo", "product_created",)

    def get_photo(self, obj):
        if obj.product_image:
            try:
                return mark_safe(f'<img src="{obj.product_image.all()[0].product_image.url}" width="75">')
            except:
                return '-'
        else:
            return '-'

    get_photo.short_description = 'Rasmi'

admin.site.register(Navigation)
admin.site.register(News)
# admin.site.register(Category)
# admin.site.register(Product)
# Register your models here.
