import csv
from django.http import Http404
from django.shortcuts import render, redirect

from random import randrange

from .models import Characters, RequestLog
from .utils import get_chars, get_char


def index(request, message=None):
    characters_list = Characters.objects.order_by('name')
    context = {
        'characters_list': characters_list,
        'message': message
    }

    return render(request, 'starwars/index.html', context)


def character(request, character_id):
    try:
        character = Characters.objects.get(pk=character_id)
        context = {
            'character': character,
        }
    except Characters.DoesNotExist:
        raise Http404("Character does not exist")
    return render(request, 'starwars/details.html', context)


def search(request):
    search_string = request.POST.get('search')
    if not search_string:
        raise Http404("Search string not set")

    chars = get_chars()

    matching = [s for s in list(chars) if search_string.lower() in s]

    context = {}

    if matching:
        found_characters = []
        for entry in matching:
            found_characters.append(Characters(
                id=chars[entry],
                name=entry
            ))
        context['found_characters'] = found_characters

    return render(request, 'starwars/search.html', context)


def add_from_swapi(request, character_id):
    character_id = int(character_id)
    char_data = get_char(character_id)
    if not char_data:
        raise Http404("Character not found")

    char = Characters(
        id=character_id,
        name=char_data.name,
        height=char_data.height,
        mass=char_data.mass,
        hair_color=char_data.hair_color,
        skin_color=char_data.skin_color,
        eye_color=char_data.eye_color,
        birth_year=char_data.birth_year,
        gender=char_data.gender,
    )

    char.save()

    return redirect('index')


def crud(request):
    id = request.POST.get('exist_char_id')
    trigger_save = False
    trigger_delete = request.POST.get('delete')
    message = []

    if trigger_delete:
        Characters.objects.get(pk=id).delete()
        return redirect('index')

    if id:
        action = 'update'
        char = Characters.objects.get(pk=id)
        char.action = action

    else:
        action = request.POST.get('action')
        if not action:
            action = 'add'
        id = request.POST.get('id')
        if not id:
            id = randrange(10, 100000)
        name = request.POST.get('name', '')
        height = request.POST.get('height', 'unknown')
        mass = request.POST.get('mass', 'unknown')
        hair_color = request.POST.get('hair_color', 'unknown')
        skin_color = request.POST.get('skin_color', 'unknown')
        eye_color = request.POST.get('eye_color', 'unknown')
        birth_year = request.POST.get('birth_year', 'unknown')
        gender = request.POST.get('gender', 'n/a')

        trigger_save = request.POST.get('trigger_save')

        char = Characters(
            id=id,
            name=name,
            height=height,
            mass=mass,
            hair_color=hair_color,
            skin_color=skin_color,
            eye_color=eye_color,
            birth_year=birth_year,
            gender=gender
        )

    if trigger_save and len(char.name) > 0:
        char.save()
        return redirect('character', character_id=id)

    if action == 'update':
        message.append('update character %s' % char.name)
    if action == 'add':
        message.append('add character')

    if len(char.name) == 0:
        message.append('character name is needed')

    context = {
        'message': message,
        'char': char,
        'action': action
    }

    return render(request, 'starwars/crud.html', context)

def request_log(request):
    requests = RequestLog.objects.order_by('id')[:10]
    context = {
        'requests': requests
    }
    return render(request, 'starwars/request_log.html', context)