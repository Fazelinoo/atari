from django import forms

class CheckoutForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea, label="آدرس")
    phone_number = forms.CharField(label="شماره تماس")
