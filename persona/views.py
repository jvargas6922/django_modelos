from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

# Create your views here.
def index(request):
    personas = Persona.objects.all()
    context ={'personas':personas}
    return render(request, 'persona/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        persona = Persona(name=name,last_name=last_name,email=email,age=age)
        persona.save()
        return HttpResponse('Persona creada correctamente')
    
    return render(request, 'persona/create.html')