from django.shortcuts import render, HttpResponse


# Create your views here.
def entrada(request):

    html_basico = """
    <h1> Mi pagina web</h1>
    <h2> <a href = "/home"> Pagina Principal </a> </h2>
    <h2> <a href = "/portafolio"> Portafolio </a> </h2>
    <h3> <a href = "/contact"> Contacto </a> </h3>
    <h2> <a href = "/about"> Acerca De Mi </a> </h2>
    """

    return HttpResponse(html_basico)

def home(request):
    html_response = "<h1> My web personal</h1><h2> Portada </h2><p> Subcabecera </p>"
    return HttpResponse(html_response)

def about(request):
    html_response = "<p> Esta es la información extra de la parte de abajo de la página web </p>"
    return HttpResponse(html_response)

def portafolio(request):
    html_response = "<p> Aqui se puede encontrar la informacion del portafolio </p>"
    return HttpResponse(html_response)

def contacto(request):
    html_response = """
    <h1> Aqui se puede encontrar la informacion del contacto! </h1> 
    <p> Aqui esta mi email para preguntarme dudas: <a href= "joaquinmarpas@gmail.com"> Contacto </a> </p>
    """
    return HttpResponse(html_response)