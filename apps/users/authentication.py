from datetime import timedelta

from django.utils import timezone
from django.conf import settings
from django.contrib.sessions.models import Session

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):
    
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expired_handler(self, token):
        is_expire = self.is_token_expired(token)

        if is_expire:
            user = token.user
            all_sessions = Session.objects.filter(expire_date__gte=timezone.now())

            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if user.id == int(session_data.get("_auth_user_id")):
                        session.delete()
            
            token.delete()
            token = self.get_model().objects.create(user=user)
            
        return token

    def authenticate_credentials(self, key):
        user = None
        
        try:
            token = self.get_model().objects.select_related("user").get(key=key)
            token = self.token_expired_handler(token)
            user = token.user
        except self.get_model().DoesNotExist:
            pass

        return user