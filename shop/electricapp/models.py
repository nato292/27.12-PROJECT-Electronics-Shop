from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='products/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)     

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name='shipping_address')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city}, {self.address}"