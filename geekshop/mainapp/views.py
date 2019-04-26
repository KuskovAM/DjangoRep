from django.shortcuts import render

# Create your views here.
def main(requset):
    return render(requset, 'mainapp/index.html')

def catalog(requset):
    return render(requset, 'mainapp/catalog.html')

def contacts(requset):
    return render(requset, 'mainapp/contacts.html')

def mapet(request):
    return render(request,'mainapp/products/C50.html')