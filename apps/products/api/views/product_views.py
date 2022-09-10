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

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.get_queryset().select_related("measure_unit", "category_product").get(pk=kwargs["pk"])
        )
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status=True)

    def delete(self, request, *args, **kwargs):
        product = self.get_queryset().filter(pk=kwargs["pk"]).first()

        if product:
            product.status = False
            product.save()
            return Response({"data": "Product deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"data": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status=True)

    def patch(self, request, *args, **kwargs):
        product = self.get_queryset().filter(pk=kwargs["pk"]).first()

        if product:
            serializer = self.serializer_class(product, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"data": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        product = self.get_queryset().filter(pk=kwargs["pk"]).first()

        if product:
            serializer = self.serializer_class(product, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"data": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
