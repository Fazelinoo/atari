from django import forms

class CheckoutForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label="آدرس")
    phone_number = forms.CharField(label="شماره تماس", max_length=15)
