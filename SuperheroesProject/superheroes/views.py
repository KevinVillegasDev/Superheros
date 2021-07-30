from django.shortcuts import render
from .models import Superhero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.



def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, superhero_id):
    a_hero = Superhero.objects.get(pk=superhero_id)
    context = {
        'a_hero': a_hero
    }
    return render(request, 'superheroes/details.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superhero_ability = request.POST.get('primary_superhero_ability')
        secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_superhero_ability=primary_superhero_ability, 
                                  secondary_superhero_ability=secondary_superhero_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')