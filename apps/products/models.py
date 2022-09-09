from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel


class MeasureUnit(BaseModel):

    description = models.CharField("Description", max_length=100, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "unit of measurement"
        verbose_name_plural = "units of measurement"

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):

    description = models.CharField("Description", max_length=100, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Category of product"
        verbose_name_plural = "Categories of product"

    def __str__(self):
        return self.description


class OfferIndicator(BaseModel):

    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(
        CategoryProduct, verbose_name="Category of product", on_delete=models.CASCADE, null=False, related_name="offers"
    )
    historical = HistoricalRecords()

    class Meta:
        verbose_name = "Offer indicator"
        verbose_name_plural = "Offer indicators"

    def __str__(self):
        return f"Category offer {self.category_product}: {self.discount_value}%"


class Product(BaseModel):
    name = models.CharField("Name of product", max_length=150, blank=False, null=False, unique=True)
    description = models.CharField("Description", max_length=100, blank=False, null=False)
    image = models.ImageField("Image of prducts", upload_to="products/", blank=True, null=True)
    measure_unit = models.ForeignKey(
        MeasureUnit, verbose_name="Unit of measurement", on_delete=models.CASCADE, null=True, related_name="products"
    )
    category_product = models.ForeignKey(
        CategoryProduct, verbose_name="Category of product", on_delete=models.CASCADE, null=True, related_name="products"
    )

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
