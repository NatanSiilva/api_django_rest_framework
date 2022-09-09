from apps.base.api import *
from apps.products.api.serializer.product_serializers import *


class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset().select_related('measure_unit', 'category_product')
        return queryset
  
