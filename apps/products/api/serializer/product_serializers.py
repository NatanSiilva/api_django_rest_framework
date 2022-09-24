from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializer.general_serializers import *

class ProductSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/
    # measure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()

    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ("status", 'created_at', 'updated_at', 'deleted_date')


    def validate_measure_unit(self, value):
        # obrigando que os value nao seja vazio
        if not value:
            raise serializers.ValidationError("measure_unit is required")
        return value

    def validate_category_product(self, value):
        if not value:
            raise serializers.ValidationError("category_product is required")
        return value

    def validate(self, data):
        # obrigando que envie os parametros
        if not data.get('measure_unit'):
            raise serializers.ValidationError({"measure_unit": "measure_unit is required"})

        if not data.get('category_product'):
            raise serializers.ValidationError({"category_product": "category_product is required"})

        return data

    def to_representation(self, instance):
            
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url if instance.image else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit else '',
            'category_product': instance.category_product.description if instance.category_product else '',
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
        }