"""
Vamos a crear un middleware que verifique la ip del usuario y ver
si lo dejamos pasar
"""

"""
Los middlewares recibe un parametro llamando get_response
"""

#pip install django-ipware
#pip install requests
from ipware import get_client_ip
from django.http import HttpResponse
from .models import IPregistradas
#BLACK_LIST=['127.0.0.1']







class IPIsValid:

    #__init__ : sirve como constructor
    #__call__ : se ejecuta antes de mostrar la vista
 

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print(ip, type(ip))
        response = self.get_response(request)
        IPregistradas.objects.create(ip=ip)
        
        return response

            
""" 
def is_valid_ip(get_response):
    
    #Esta funcion is_valid_ip va a retornar otra funcion
    #porque necesitamos comprobar que exista una respuesta al cliente
    #Puden 2 tipos de respuesta 

    #success: 201, 200
    #error: 500, 404, 403, 401
    
    
    
    #Esta funcion ya recibe request 
    
    def middleware(request):
        ip=get_client_ip(request)
        print("ip", ip[0])
        response=get_response(request)

        if ip in BLACK_LIST:
            return HttpResponse("no tienes permiso", status=404)
        
        return response
    
    return middleware
 """
#pip install django-ipware
