import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("apps.users.api.urls")),
    path("api/products/", include("apps.products.api.routers")),
]

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
] + urlpatterns
