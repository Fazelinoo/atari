"""
URL configuration for attari project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from django.views.generic import TemplateView


from .sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {'static': StaticViewSitemap,
}



urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name='home_app/robots.txt', content_type='text/plain')),
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('daroos/', include('Daroos_app.urls')),
    path('accounts/', include('accounts.urls')),

    path('cart/', include('cart_app.urls')),

    path('admiin', include('admin_app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
