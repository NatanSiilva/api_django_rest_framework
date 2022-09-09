from django.contrib import admin
from apps.products.models import *


@admin.register(MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "status")


@admin.register(OfferIndicator)
class OfferIndicatorAdmin(admin.ModelAdmin):
    list_display = ("id", "discount_value", "status", 'category_product', 'historical')


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "status", 'historical')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "measure_unit", "category_product", "status")
