from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.users.api.serializers import *


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    update_serializer_class = UpdateUserSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

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
            return Response("User created successfully", status=status.HTTP_201_CREATED)
        return Response({"message": "error", "status": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        serializer = self.serializer_class(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        serializer = self.update_serializer_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("User updated successfully", status=status.HTTP_200_OK)
        return Response({"message": "error", "status": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = self.get_object(pk)

        if not user:
            return Response({"message": "error", "status": "user not found"}, status=status.HTTP_404_NOT_FOUND)

        user.is_active = False
        user.save()

        return Response("User deleted successfully", status=status.HTTP_200_OK)