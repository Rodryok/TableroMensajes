from django.shortcuts import render
from .models import Mensaje
from django.contrib.auth.models import User

def mensajes_recibidos(request):
    usuario = request.user
    mensajes = Mensaje.objects.filter(destinatario=usuario)
    return render(request, 'mensajes/recibidos.html', {'mensajes': mensajes})