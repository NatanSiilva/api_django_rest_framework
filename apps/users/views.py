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
        refresh_token = request.data.get("refresh_token")
        print(refresh_token)

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()

                return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
