from rest_framework import status
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.authentication_mixins import AuthenticationMixins


# @authentication_classes([AuthenticationMixins])
@api_view(["GET", "POST"])
def user_api_view(request):
    if request.method == "GET":

        users = User.objects.all().values('id', 'username', 'email', 'name', 'password')
        user_serializer = UserListSerializer(users, many=True)

        return Response(
            {"data": user_serializer.data, "message": "Users retrieved successfully"}, status=status.HTTP_200_OK
        )

    elif request.method == "POST":

        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                {"data": user_serializer.data, "message": "User created successfully"}, status=status.HTTP_201_CREATED
            )

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @authentication_classes([AuthenticationMixins])
@api_view(["GET", "PUT", "DELETE"])
def user_detail_api_view(request, pk=None):
    user = User.objects.filter(id=pk).first()

    if user:
        if request.method == "GET":
            if pk is not None:
                user_serializer = UserSerializer(user)
                return Response(
                    {"data": user_serializer.data, "message": "User retrieved successfully"}, status=status.HTTP_200_OK
                )
            return Response({"data": "Not found"})

        elif request.method == "PUT":
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(
                    {"data": user_serializer.data, "message": "User updated successfully"}, status=status.HTTP_200_OK
                )

            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            user.delete()
            return Response({"data": "User deleted"}, status=status.HTTP_200_OK)

    return Response({"data": "Not found"}, status=status.HTTP_404_NOT_FOUND)


# class UserAPIView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)

#         return Response({"data": serializer.data})
