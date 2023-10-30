"""reflex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.conf.urls import url
from django.urls import include, re_path

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from hotel import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page':'/'}),
    re_path(r'^accounts/signup/$', views.signup, name='signup'),
    re_path(r'', include(('hotel.urls', 'hotel'), namespace='hotel')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)