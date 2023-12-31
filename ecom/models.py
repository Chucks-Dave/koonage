from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    name = models.CharField(max_length=40)
    product_image = models.ImageField(
        upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Confirmed', 'Order Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=20, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)


class Feedback(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Staff(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    staff_member = models.ForeignKey('Staff', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    email = models.EmailField(default='@example.com')  # Add 'email' field
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.date} at {self.time} with {self.staff_member.name} for {self.customer}"
