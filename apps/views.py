from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from root import settings
from .filters import CategoryFilter
from .models import Category, Product, User
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter
from .serializers import CategorySerializer, ProductSerializer, RegisterModelSerializer, UserRegisterModelSerializer


class UserRegistrationAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterModelSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        email_subject = 'Ro\'yxatdan o\'tdingiz'
        email_message = 'Siz ro\'yxatdan o\'tdingiz.'
        send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [user.email])
        return Response({'message': 'Foydalanuvchiga xabar yuborildi.'},
                        status=status.HTTP_201_CREATED)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    filterset_class = CategoryFilter


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
