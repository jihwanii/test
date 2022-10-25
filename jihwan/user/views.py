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
def index(request):
    return render(request, "index.html")

def register_mainView(request):
    return render(request, "register_main.html")

def register(request):
    return render(request, '../templates/register.html')

class Seller_register(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'seller_rigester.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class buyer_register(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'buyer_rigester.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
        
def loginView(request):
    pass

def logoutView(request):
    logout(request)
    return redirect("home")