from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            return redirect('/')
        else:
            error = "نام کاربری یا رمز عبور اشتباه است."
    return render(request, 'accounts/accounts.html', {'error': error})

def log_out(request):
    logout(request)
    return redirect('/')




# def signin(request):
#     context = {"errors": []}
#     if request.user.is_authenticated == True:
#         return redirect('/')
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         number = request.POST.get("number")

        
#         user = User.objects.create(username=username, password=password)
        
#         login(request, user)
#         return redirect('/')
#     return render(request, 'accounts/singnin.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/singnin.html', {'form': form})

def search(request):



    q = request.GET.get('q')
    




# views.py

@login_required
def user_detail_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'accounts/showinfo.html', {'user': user})
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('')