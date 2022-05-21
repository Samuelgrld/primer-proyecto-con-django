#vistas que controlan el programa osea botones y links y esas cosas que modifican lo que se ve
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def hello_world(request):
    return HttpResponse("hello world, estas en django")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre, edad):

      documentoDeTexto = f"Mi nombre es: {nombre} <br><br> mi edad es {edad}"


      return HttpResponse(documentoDeTexto)

def miAño(self, edad):
    
    AñoActual = datetime.datetime.now().year
    añoDeNacimiento = AñoActual - int(edad)
    
    return HttpResponse(f'mi año de nacimiento es {añoDeNacimiento}')


def probandoTemplate(self):

    miHtml = open("/home/samuel/example/PrimerProyecto/PrimerProyecto/templates/template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)