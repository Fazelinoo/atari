from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(label="نام", max_length=50)
    last_name = forms.CharField(label="نام خانوادگی", max_length=50)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label="آدرس")
    phone_number = forms.CharField(label="شماره تماس", max_length=15)
