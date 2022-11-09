from django.http import HttpResponse
from appvazquez.models import Familia 
from django.template import Template, Context

def lista_de_familiares(request):
    familiares = Familia.objects.all()
    response = ""
    for familia in familiares:
        response += f"({familia.nombre} {familia.apellido},{familia.edad})" + " | "

    return HttpResponse(response)
    
def plantilla2(request):
    archivo = open("C:/Users/Vazqu/OneDrive/Desktop/Proyecto_Familiares/Main/appvazquez/Templates/Plantilla_familia.html")
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
