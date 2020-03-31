from django import forms
from django_countries import fields
from django_countries.widgets import CountrySelectWidget

PAYENT_CHOICE =(
    ('S','Stripe'),
    ('P','Paypal')
)

class CheckoutForm(forms.Form):
    street_adress =forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'1234 Main St',
        'class':"form-control"
    }))
    appartement_adress = forms.CharField(required = True, widget=forms.TextInput(attrs={
        'placeholder':"Apartment or suite",
        'class':"form-control"
    }))
    country = fields.CountryField(blank_label= "(select country)").formfield(
        widget = CountrySelectWidget(attrs = {
        'class' :"custom-select d-block w-100"
    }))
    zip = forms.CharField(widget= forms.TextInput(attrs = {
        'class':"form-control",
        'id':"zip"
    }))
    same_shipping_adress =forms.BooleanField(required= False)
    save_info =forms.BooleanField(required= False)
    payment_option = forms.ChoiceField(widget = forms.RadioSelect , choices= PAYENT_CHOICE)
class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))
