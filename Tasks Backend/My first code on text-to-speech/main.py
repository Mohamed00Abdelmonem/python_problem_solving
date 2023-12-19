from django.shortcuts import render
from .models import Product
# Create your views here.
def home(requset):
    return render(requset, 'products/home.html')


def about(requset):
    return render(requset, 'products/about.html')



# def Electronics(requset):
#     # Electronics = Product.objects.all()
#
#     # this is a conditioon becouse showing products Electronics only (Mohamed)
#
#     Electronics = Product.objects.filter(section__name__contains='Electronics')
#     context = {'Electronics': Electronics}
#     return render(requset, 'products/products.html', context)



def Furniture(requset):
    furniture = Product.objects.filter(section__name__contains='Furniture')
    context = {'furniture': furniture}
    return render(requset, 'products/furniture.html', context)

#
#
#
# def Clothes(requset):
#
#     Clothes = Product.objects.filter(section__name__contains='Clothes')
#     context = {'Clothes': Clothes}
#     return render(requset, 'products/clothes.html', context)



def furniture(requset):
    return render(requset, 'products/furniture.html')

def clothes(requset):
    return render(requset, 'products/clothes.html')

def Electronics(requset):
    return render(requset, 'products/products.html')
