from rest_framework import status
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = (
                self.serializer_class()
                .Meta.model.objects.filter(is_active=True)
                .values("id", "username", "email", "name", "password")
            )
        return self.queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('User created successfully', status=status.HTTP_201_CREATED)
        return Response({"message": 'error', "status": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    