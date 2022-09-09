import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("apps.users.api.urls")),
    path("api/product/", include("apps.products.api.urls")),
]


urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
] + urlpatterns
