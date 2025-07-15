from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from admin_app.forms import ProductForm


from cart_app.models import Order

# Create your views here.

def admiin(request):
    orders = Order.objects.all().order_by('-created_at')



    return render(request, 'admin_app/admiin.html', {'orders': orders})


def delete_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        order.delete()
    return redirect('admiin')  # مطابق با نام url نمایش پنل مدیریت
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admiin')
    else:
        form = ProductForm()
    
    return render(request, 'admin_app/add_product.html', {'form': form})



@require_POST
def toggle_payment_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_sent = not order.is_sent
    order.save()
    return redirect('admiin')
