from django.http import Http404
from django.shortcuts import render


from .models import Characters


def index(request):
    characters_list = Characters.objects.order_by('name')
    context = {
        'characters_list': characters_list,
    }
    return render(request, 'starwars/index.html', context)


def character(request, character_id):
    try:
        character = Characters.objects.get(pk=character_id)
        context = {
            'character': character,
        }
    except Characters.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'starwars/details.html', context)