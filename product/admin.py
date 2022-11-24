from django.contrib import admin

from .models import Category, Brand, Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':['name']}


