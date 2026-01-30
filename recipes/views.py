from django.shortcuts import render
from django.http import HttpResponse

# o request recebe a requisição feita pelo usuário exemplo site.com/sobre é uma requisição  
def home(request):
    return HttpResponse("Hello, World!")  