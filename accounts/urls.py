from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login', views.login_view, name='login'),

    path('logout', views.log_out, name='logout'),

    path("signin", views.signin, name='signin'),

    path('user/<str:username>/', views.user_detail_view, name="info"),

    path('password/change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),


]
