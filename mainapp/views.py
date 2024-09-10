from django.shortcuts import render
from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket

def index(request, pk=None):
  product_list = Product.objects.all()
  product_category = ProductCategory.objects.all()
  
  basket = []
  if request.user.is_authenticated:
    basket = Basket.objects.filter(user=request.user)

  if pk:
    if pk == '0':
      product_list = Product.objects.all().order_by('price')
      
  else:
    
    products = Product.objects.filter(category__pk=pk).order_by('price')
  context = {
    'products': product_list,
    'product_category': product_category,
    'basket': basket
  }

  return render(request, 'mainapp/index.html', context)
