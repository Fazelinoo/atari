from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from Daroos_app.models import Daroo
from cart_app.form import CheckoutForm
from .models import Order, OrderItem
@staff_member_required
def all_orders(request):
    if request.method == "POST":
        if 'delete_order_id' in request.POST:
            order_id = request.POST.get('delete_order_id')
            order = get_object_or_404(Order, id=order_id)
            order.delete()
            return redirect('all_orders')

    orders = Order.objects.prefetch_related('items__product').all()
    return render(request, 'cart_app/all_orders.html', {'orders': orders})




def cart_add(request, product_id):
    
    product = get_object_or_404(Daroo, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('cart_detail')
def cart_detail(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    cart = request.session.get('cart', {})
    products = Daroo.objects.filter(id__in=cart.keys())
    cart_items = []

    cart_total = 0
    for product in products:
        quantity = cart.get(str(product.id), 0)
        total_price = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price,
        })
        cart_total += total_price

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart_app/cart_deatils.html', context)
def cart_update(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[str(product_id)] = quantity
        else:
            cart.pop(str(product_id), None)

        request.session['cart'] = cart

    return redirect('cart_detail')



def cart_remove(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart.pop(str(product_id), None)  # حذف محصول اگر موجود باشه
        request.session['cart'] = cart

    return redirect('cart_detail')





def checkout(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    cart = request.session.get('cart', {})

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']

            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone_number=phone_number
            )

            for product_id, quantity in cart.items():
                try:
                    product = Daroo.objects.get(id=product_id)
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        first_name=first_name,
                        last_name=last_name,
                        quantity=quantity
                    )
                except Daroo.DoesNotExist:
                    continue

            request.session['cart'] = {}
            return redirect('order_success')
    else:
        form = CheckoutForm()

    return render(request, 'cart_app/checkout.html', {'form': form})



def order_success(request):
    return render(request, 'cart_app/order_success.html')


@login_required

def my_orders(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product').order_by('-created_at')
    return render(request, 'cart_app/jaris_sefaresh.html', {'orders': orders})
@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.is_sent:
        # اجازه حذف داده نشود یا پیام بده
        return redirect('my_orders')
    if request.method == 'POST':
        order.delete()
        return redirect('my_orders')
    # می‌تونی یک صفحه تایید هم بسازی یا مستقیما حذف کنی
    return redirect('my_orders')