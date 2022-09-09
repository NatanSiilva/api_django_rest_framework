from django.urls import path
from apps.products.api.views.general_views import *

urlpatterns = [
    path('measure_units/', MeasureUnitListAPIView.as_view(), name='measure_units'),
    path('offer_indicators/', OfferIndicatorListAPIView.as_view(), name='offer_indicators'),
    path('category_products/', CategoryProductListAPIView.as_view(), name='category_products'),
]
 