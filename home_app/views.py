from django.shortcuts import get_object_or_404, render
from Daroos_app.models import Daroo

def Home(request):
    daroo = Daroo.objects.all()
    return render(request, 'home_app/atari.html', context={'Daroos': daroo})

def product_detail(request, pk):
    product = get_object_or_404(Daroo, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def category_products(request, category_name):
    products = Daroo.objects.filter(category__iexact=category_name)
    return render(request, 'home_app/side_bar.html', {
        'products': products,
        'category_name': category_name
    })



