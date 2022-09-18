from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

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
    # queryset = CategoryProduct.objects.filter(status=True)

    def get_queryset(self):
        queryset = self.get_serializer().Meta.model.objects.filter(status=True)
        return queryset

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs["pk"], status=True)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        if self.get_object().exists():
            instance = self.get_object().get()
            serializer = self.serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if self.get_object().exists():
            instance = self.get_object().get()
            instance.delete()
            return Response({"message": "CategoryProduct destroy"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "CategoryProduct not found"}, status=status.HTTP_404_NOT_FOUND)
