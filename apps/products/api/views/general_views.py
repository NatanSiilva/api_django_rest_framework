from rest_framework import viewsets

from apps.base.api import GeneralListAPIView
from apps.products.models import *
from apps.products.api.serializer.general_serializers import *


class MeasureUnitViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing measure units.
    """
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnit.objects.filter(status=True)


class OfferIndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = OfferIndicatorSerializer
    queryset = OfferIndicator.objects.filter(status=True)


class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = CategoryProduct.objects.filter(status=True)
