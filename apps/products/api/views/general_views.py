from apps.base.api import GeneralListAPIView
from apps.products.models import *
from apps.products.api.serializer.general_serializers import *


class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer


class OfferIndicatorListAPIView(GeneralListAPIView):
    serializer_class = OfferIndicatorSerializer


class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer
