from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from .models import Category, Product, User
from rest_framework.fields import CharField, EmailField
from rest_framework.exceptions import ValidationError


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class UserRegisterModelSerializer(ModelSerializer):
    password_confirm = CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise ValidationError("Parollar mos kelmadi")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class RegisterModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    email = EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError('Bu email bazada bor')
        return value

    def validate(self, data):
        confirm_password = data.pop('confirm_password')
        if confirm_password and confirm_password == data['password']:
            data['password'] = make_password(data['password'])
            data['is_active'] = False
            return data
        raise ValidationError("Parol mos emas")
