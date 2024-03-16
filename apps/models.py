from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ForeignKey, TextField, CASCADE, DecimalField, UUIDField
from django_resized import ResizedImageField
import uuid


class User(AbstractUser):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)


class Category(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(max_length=100)


class Product(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(max_length=100)
    category = ForeignKey(Category, related_name='products', on_delete=CASCADE)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=2)
    owner = CharField(max_length=100)


class ProductPhoto(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    product = ForeignKey(Product, related_name='photos', on_delete=CASCADE)
    image = ResizedImageField(size=[736, 736], crop=['middle', 'center'], upload_to='products', blank=True,
                              null=True)
