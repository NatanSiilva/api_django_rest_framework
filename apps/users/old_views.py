from datetime import datetime

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from apps.users.api.serializers import UserTokenSerializer

from django.contrib.sessions.models import Session
from apps.users.authentication_mixins import AuthenticationMixins


class RefreshToken(AuthenticationMixins, APIView):
    def get(self, request):
        # username = request.data["username"]
        try:
            # user = UserTokenSerializer.Meta.model.objects.filter(username=self.user.username).first()
            user_token,_ = Token.objects.get_or_create(user=self.user)
            user = UserTokenSerializer(self.user)
            return Response({"token": user_token.key, "user": user.data}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})

        if serializer.is_valid():
            user = serializer.validated_data["user"]

            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)

                if created:
                    return Response(
                        {
                            "data": {
                                "token": token.key,
                                "user": user_serializer.data,
                            },
                            "message": "User logged in successfully",
                        },
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())

                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get("_auth_user_id")):
                                session.delete()

                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response(
                        {
                            "data": {
                                "token": token.key,
                                "user": user_serializer.data,
                            },
                            "message": "User logged in successfully",
                        }
                    )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Token already exists"}, status=status.HTTP_200_OK)


class Logout(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get("token")
            token = Token.objects.filter(key=token).first()

            if token:
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())

                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get("_auth_user_id")):
                            session.delete()

                token.delete()

                session_message = "User logged out successfully"
                token_message = "Token deleted successfully"

                return Response(
                    {
                        "data": {
                            "session_message": session_message,
                            "token_message": token_message,
                            "url_login": "/login/",
                        }
                    }
                )
            else:
                return Response({"message": "Token not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
