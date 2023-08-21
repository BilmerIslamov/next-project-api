from django.contrib import admin
from .models import *


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)
    prepopulated_fields = {'slug': ('category_title',)}

@admin.register(Category)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)
    prepopulated_fields = {'slug': ('category_title',)}


admin.site.register(Navigation)
admin.site.register(News)
# admin.site.register(Category)
admin.site.register(Product)
# Register your models here.
