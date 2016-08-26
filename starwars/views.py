from django.core.cache import cache
from django.http import Http404
from django.shortcuts import render

import swapi


from .models import Characters
from .utils import get_char_cache_key, get_chars, get_char


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
        raise Http404("Character does not exist")
    return render(request, 'starwars/details.html', context)


def search(request):
    search_string = request.POST.get('search')
    if not search_string:
        raise Http404("Search string not set")

    chars = get_chars()

    matching = [s for s in list(chars) if search_string in s]

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
        raise Http404("Character not saved")

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

    return render(request, 'starwars/api_add.html', context)