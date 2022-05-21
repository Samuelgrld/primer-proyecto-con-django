"""PrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from PrimerProyecto.views import (
    hello_world,
    miNombreEs, 
    segunda_vista, 
    diaDeHoy,
    miAño,
    probandoTemplate
)


urlpatterns =[
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world), #el primer hello world es el nombre de la url y el segundo es la respuesta que da, osea la funcion que esta en views que se llama hello_world
    path('segundavista/',segunda_vista),
    path('diaDeHoy/',diaDeHoy),
    path('miNombreEs/<nombre>/<edad>', miNombreEs),
    path('miAño/<edad>',miAño),
    path('probandoTemplate',probandoTemplate)
]
