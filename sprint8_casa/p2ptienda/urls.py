"""p2ptienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from p2pApp.views import Carrazo
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from usuario.views import RegistroUsuario,Login,logoutUsuario
from django.contrib.auth.decorators import login_required
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/',include(('p2pApp.urls','p2pApp'))),
    path('registrar/',RegistroUsuario.as_view(),name='registrar'), 
    path('accounts/login/',Login.as_view(),name ='login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    
 ] 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
