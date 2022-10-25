from telnetlib import SE
from django.contrib.auth.forms import UserCreationForm
from jihwan.models import *
from django import forms
from django.db import transaction

class SellerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    post_code = forms.CharField(required=True)
    address = forms.CharField(required=True)
    detail_address = forms.CharField(required=True)
    company_document = forms.FileField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.phone_number = self.cleaned_data.get('phone_number')
        user.post_code = self.cleaned_data.get('post_code')
        user.address = self.cleaned_data.get('address')
        user.detail_address = self.cleaned_data.get('detail_address')
        user.save()
        seller = Seller.objects.create(user=user)
        seller.company_document=self.cleaned_data.get('company_document')
        seller.save()
        return user


class BuyerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    post_code = forms.CharField(required=True)
    address = forms.CharField(required=True)
    detail_address = forms.CharField(required=True)
    company_document = forms.FileField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.phone_number = self.cleaned_data.get('phone_number')
        user.post_code = self.cleaned_data.get('post_code')
        user.address = self.cleaned_data.get('address')
        user.detail_address = self.cleaned_data.get('detail_address')
        user.save()
        buyer = Buyer.objects.create(user=user)
        buyer.company_document=self.cleaned_data.get('company_document')
        buyer.save()
        return user


