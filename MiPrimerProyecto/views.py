from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def saludo(request):
    return HttpResponse('Hola a todos desde El Nochero')

def segunda_vista(req):
    return HttpResponse(
        """
        <h1>Bienvenido a mi pagina</h1>
        <br>
        <br>
        <p>Vamos avanzando</p>
        """
    )

def dia_hoy(req):
    dia=datetime.now()
    documento = f'Hoy es: {dia}'
    return HttpResponse(documento)

def saluda_con_nombre(req, nombre):
    documento = f'Hola {nombre}'
    return HttpResponse(documento)

def probando_template(req):
    miHtml = open("C:\Dev\Python\Entrega3\MiPrimerProyecto\MiPrimerProyecto\templates\template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()

    miContexto = Context()
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)