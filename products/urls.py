from django.urls import path
from . import views
from .views import ProductListAPIView

urlpatterns = [
    path("", views.ProductListAPIView.as_view(), name="product_list"),
]
