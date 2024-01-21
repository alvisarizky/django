from django.contrib import admin
from .models import Order, Products

# Register your models here.
admin.site.site_header = 'E-Commerce Site'
admin.site.site_title = 'ABC E-Commerce'
admin.site.index_title = 'Manage'

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")
    
    change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','discount','category','image')
    search_fields = ('title','category',)
    actions = ('change_category_to_default',)

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)