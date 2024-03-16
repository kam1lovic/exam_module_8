from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.views import CategoryListAPIView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, \
    UserRegistrationAPIView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('product/', ProductListCreateAPIView.as_view(), name='products'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

]
