import debug_toolbar
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import *


schema_view = get_schema_view(
    openapi.Info(
        title="Api Ecomerce Rest d",
        default_version="v0.1",
        description="Api Rest Ecomerce documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@test.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path("login/", SignIn.as_view(), name="login"),
    path("logout/", SignOut.as_view(), name="logout"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('refresh-token/', RefreshToken.as_view(), name='refresh-token'),
    path("api/user/", include("apps.users.api.routers")),
    path("api/", include("apps.products.api.routers")),
]

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
] + urlpatterns
