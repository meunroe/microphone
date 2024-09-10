from django.db import models
  
class ProductCategory(models.Model):
  name = models.CharField(verbose_name='имя', max_length=64, unique=True)
  description = models.TextField(verbose_name='описание', blank=True)
  def __str__(self):
    return self.name

class Product(models.Model):
  category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
  name = models.CharField(max_length=150, verbose_name="Name")
  image = models.ImageField(blank=True, upload_to='products')
  description = models.TextField(verbose_name="description")
  price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="price", default=0)
  quantity = models.PositiveIntegerField(default=0, verbose_name="quantity")
  
  def __str__(self):
    return f"{self.name} ({self.category.name})"