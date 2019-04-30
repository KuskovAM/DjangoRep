from django.shortcuts import render
from .models import Product, ProductCategory

# Create your views here.
def main(requset):
    return render(requset, 'mainapp/index.html')

def catalog(requset):
    return render(requset, 'mainapp/catalog.html')

def contacts(requset):
    return render(requset, 'mainapp/contacts.html')

def mapet(request):
    return render(request,'mainapp/products/C50.html')

def products(request):
    context = {'products': Product.objects.all()}
    return render(request,'mainapp/products.html', context)