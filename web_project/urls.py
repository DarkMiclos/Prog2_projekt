"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pages.views import home, gallery, contact, booking
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name = 'home'),
    path('gallery/', gallery, name = 'gallery'),
    path('contact/', contact, name = 'contact'),
    path('booking/', booking, name = 'booking'),
    path('', include('payments.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache = True, must_revalidate = True)(serve))
    #to prevent caching in debug mode