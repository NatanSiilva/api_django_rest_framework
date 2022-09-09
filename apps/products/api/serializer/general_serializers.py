from rest_framework import serializers

from apps.products.models import *


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ("status", 'created_at', 'updated_at', 'deleted_date')


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ("status", 'created_at', 'updated_at', 'deleted_date')



class OfferIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferIndicator
        exclude = ("status", 'created_at', 'updated_at', 'deleted_date')

