from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from appvazquez.views import *


def plantilla(request):
    archivo = open("C:/Users/Vazqu/OneDrive/Desktop/Proyecto_Familiares/Main/familiarescodder/Templates/plantilla.html")
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


