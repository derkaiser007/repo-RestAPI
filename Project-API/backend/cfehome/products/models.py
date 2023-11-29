from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL # auth.User
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def sale_policy(self):
        return "offer is limited"


"""
In Terminal:
python manage.py shell
from products.models import Product

Product.objects.create(title='abc', content='pqr', price=12.34)
Product.objects.create(title='lmn', content='xyz', price='78.90')
Product.objects.all().order_by("?").first()

Product.objects.last().sale_price
Product.objects.last().price

prod_obj = Product.objects.first()
user = prod_obj.user
user_products = user.product_set.all()
user
prod_obj
user_products

exit()
"""

"""
The @property decorator in Python is used to define a method as a property, allowing you to access it 
like an attribute rather than a method.
"""