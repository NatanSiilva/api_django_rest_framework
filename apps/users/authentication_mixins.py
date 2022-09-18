from rest_framework import status, exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import get_authorization_header

from apps.users.authentication import ExpiringTokenAuthentication


class AuthenticationMixins(BaseAuthentication):
    user = None

    def get_user(self, request):
        """
        Return:
            * user      : User instance
            * message   : Error message
            * None      : Token not found
        """

        token = get_authorization_header(request).split()

        if token:
            try:
                token = token[1].decode()
            except:
                return None

            token_expire = ExpiringTokenAuthentication()

            user = token_expire.authenticate_credentials(token)

            if user != None:
                self.user = user
                return user

        return None

    def authenticate(self, request):
        user = self.get_user(request)

        if user is None:
            raise exceptions.AuthenticationFailed("Token not found or expired")

        return (user, None)

    def dispatch(self, request, *args, **kwargs):

        user = self.get_user(request)

        if user is not None:
            return super().dispatch(request, *args, **kwargs)

        response = Response({"error": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
