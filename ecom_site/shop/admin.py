from django.contrib import admin
from .models import Product

admin.site.site_header = "[Django Project] E-Commerce Website"
admin.site.site_title = "[Django Project] E-Commerce Website"
admin.site.index_title = "Admin Page"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'description')
    search_fields = ('title',)
    fields = ('title', 'price', 'category', 'description')
    list_editable = ('price', 'category',)


# Register your models here.
admin.site.register(Product, ProductAdmin)
