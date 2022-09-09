from rest_framework import generics

from apps.products.models import *
from apps.products.api.serializer.general_serializers import *


class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(status=True)


class OfferIndicatorListAPIView(generics.ListAPIView):
    serializer_class = OfferIndicatorSerializer

    def get_queryset(self):
        return OfferIndicator.objects.filter(status=True)


class CategoryProductListAPIView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return CategoryProduct.objects.filter(status=True)
