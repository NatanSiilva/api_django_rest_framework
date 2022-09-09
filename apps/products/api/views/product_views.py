from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import *
from apps.products.api.serializer.product_serializers import *


class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset().select_related("measure_unit", "category_product")
        return queryset


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
