from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from apps.users.api.serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from apps.users.models import User


class SignIn(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            sing_in_serializer = self.get_serializer(data=request.data)

            if sing_in_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                data = {
                    'data': {
                        "user": user_serializer.data,
                        "access-token": sing_in_serializer.validated_data["access"],
                        "refresh-token": sing_in_serializer.validated_data["refresh"],
                        "message": "User logged in successfully",
                    } 
                }
                return Response(data, status=status.HTTP_200_OK)

            return Response(sing_in_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class SignOut(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user", 0)
        user = User.objects.filter(id=user_id)

        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "User not found"}, status=status.HTTP_401_UNAUTHORIZED)
