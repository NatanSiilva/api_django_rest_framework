from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import *
from apps.products.api.serializer.product_serializers import *


# class ProductListAPIView(GeneralListAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset().select_related("measure_unit", "category_product")
#         return queryset


class ProductCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    # queryset = ProductSerializer.Meta.model.objects.filter(status=True)

    def get_queryset(self):
        queryset = self.serializer_class.Meta.model.objects.select_related("measure_unit", "category_product").filter(
            status=True
        )
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total = queryset.count()
        serializer = self.serializer_class(queryset, many=True)
        return Response({"total": total, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status=True)


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(pk=kwargs["pk"]).first()

        if queryset:
            serializer = self.serializer_class(queryset)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


    def patch(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(pk=kwargs["pk"]).first()

        if queryset:
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(pk=kwargs["pk"]).first()

        if queryset:
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(pk=kwargs["pk"]).first()

        if queryset:
            queryset.status = False
            queryset.save()
            return Response({"data": "Product deleted"}, status=status.HTTP_200_OK)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

