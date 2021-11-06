"""frontend URL Configuration

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
from django.urls import path
from web.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio,name='inicio'),
    path('adminis', adminis,name='adminis'),
    path('registro', Registrarbtn,name='registro'),
    path('registrar', Registro,name='registrar'),
    path('apuntes/',usuApunte, name='apuntes'),
    path('apun',apunte, name='apun'),
    path('volv',volverA, name='volv'),
    path('lstapuntes/',lst_apuntes, name='listaapun'),
    path('cargaE',carga_estu, name='cargaE'),#carga de estudiantes
    path('cargaA',carga_apun, name='cargaA'),#carga de apuntes
    path('cargaP',carga_pensum, name='cargaP'),#carga de apuntes
    path('cargaC',carga_cursos, name='cargaC'),#carga de apuntes
    path('reporteH',carga_hash, name='reporteH'),#carga de reporte de tabla hash
    path('reporteG',carga_grafo, name='reporteG'),#carga de reporte de tabla hash
    path('reportePre',reporte_grafo, name='reportePre'),#carga de reporte de tabla hash
]
