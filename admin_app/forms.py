from django import forms
from Daroos_app.models import  Daroo

class ProductForm(forms.ModelForm):
    class Meta:
        model = Daroo
        fields = ['title', 'description', 'price', 'image', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

