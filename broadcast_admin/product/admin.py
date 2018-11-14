from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    field = ('__all__')
    list_display = ('prod_name', 'prod_act')

admin.site.register(Product, ProductAdmin)

