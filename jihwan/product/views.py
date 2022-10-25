from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
# madel import
from jihwan.models import *

# forms import
from jihwan.user.forms import *

# Create your views here.

def create_product(request):
    p_category = Category.objects.all()
    p_seller = Seller.objects.all()
    if request.method == "POST":
        user = Seller.objects.get(id = request.POST['user'])
        category = Category.objects.get(id = request.POST['category'])
        product_name = request.POST['product_name']
        MSRP = request.POST['MSRP']
        in_box = request.POST['in_box']
        stock = request.POST['stock']
        barcode = request.POST['barcode']
        image = request.FILES['image']
        content = request.POST['content']
        product_document = request.FILES['product_document']

        data = Product(
            user=user,
            category=category,
            product_name=product_name,
            MSRP=MSRP,
            in_box=in_box,
            stock=stock,
            barcode=barcode,
            image=image,
            content=content,
            product_document=product_document
        )
        data.save()

        return render(request, 'index.html')
    return render(request, 'create_product.html', {'p_category':p_category,'p_seller':p_seller})
