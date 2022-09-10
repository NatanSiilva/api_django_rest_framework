from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializer.general_serializers import *

class ProductSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/
    # measure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()

    class Meta:
        model = Product
        exclude = ("status", 'created_at', 'updated_at', 'deleted_date')


    def to_representation(self, instance):
            
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url if instance.image else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit else '',
            'category_product': instance.category_product.description if instance.category_product else '',
        }