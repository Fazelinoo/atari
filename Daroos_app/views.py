from django.shortcuts import render, get_object_or_404
from .models import Daroo
  # فرض بر این است که مدل محصول شما Product نام دارد



# def Daroo(request):
#     return render(request, 'Daroos_app/Daroos.html', context={})

def product_detail(request, product_id):
    product = get_object_or_404(Daroo, id=product_id)
    return render(request, 'Daroos_app/Daroos.html', {'product': product})




def search(request):

    q = request.GET.get('q')
    darro = Daroo.objects.filter(title__icontains=q)
    return render(request, "Daroos_app/serch_result.html", context={"product": darro})