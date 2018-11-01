from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    field = ('__all__')

admin.site.register(Product, ProductAdmin)

