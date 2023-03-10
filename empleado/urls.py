"""empleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# agregamos re_path y include
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #vinculamos el archivo principal de urls con cada una de las aplicaciones que creamos
    # re_path('', include("applications.departamentos.urls")),
    #llamamps al proyecto esas url
    re_path('', include("applications.personas.urls")),
    re_path('', include("applications.departamento.urls")),
    re_path('', include("applications.home.urls")),
    
]
