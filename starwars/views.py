import csv
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse


from random import randrange

from .forms import CharacterForm, CharacterItemForm
from .models import Characters, RequestLog
from .utils import get_chars, get_char


@login_required(login_url='/starwars/login/')
def index(request):

    characters_list = Characters.objects.order_by('name')
    context = {
        'characters_list': characters_list
    }

    return render(request, 'starwars/index.html', context)


@login_required(login_url='/starwars/login/')
def character(request, character_id):
    try:
        character = Characters.objects.get(pk=character_id)
        context = {
            'character': character,
        }
    except Characters.DoesNotExist:
        raise Http404("Character does not exist")

    return render(request, 'starwars/details.html', context)


@login_required(login_url='/starwars/login/')
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


@login_required(login_url='/starwars/login/')
def edit(request, character_id):
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            char = Characters(
                id=character_id,
                name=request.POST['name'],
                height=request.POST['height'],
                mass=request.POST['mass'],
                hair_color=request.POST['hair_color'],
                skin_color=request.POST['skin_color'],
                eye_color=request.POST['eye_color'],
                birth_year=request.POST['birth_year'],
                gender=request.POST['gender']
            )
            if request.FILES.get('pic'):
                char.pic = request.FILES['pic']
            char.save()
            return redirect('character', character_id=character_id)

    else:
        char = Characters.objects.get(pk=character_id)
        form = CharacterItemForm(instance=char)

    context = {
        'form': form,
        'action': reverse('edit', args=(character_id,))
    }

    return render(request, 'starwars/form.html', context)


@login_required(login_url='/starwars/login/')
def delete(request, character_id):
    Characters.objects.get(pk=character_id).delete()
    return redirect('index')


@login_required(login_url='/starwars/login/')
def add(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            char_id = randrange(10, 100000)
            char = Characters(
                id=char_id,
                name = request.POST['name'],
                height = request.POST['height'],
                mass = request.POST['mass'],
                hair_color = request.POST['hair_color'],
                skin_color = request.POST['skin_color'],
                eye_color = request.POST['eye_color'],
                birth_year = request.POST['birth_year'],
                gender = request.POST['gender']
            )
            if request.FILES.get('pic'):
                char.pic = request.FILES['pic']
            char.save()
            return redirect('character', character_id=char_id)

    else:
        form = CharacterForm()

    context = {
        'form': form,
        'action': reverse('add')
    }

    return render(request, 'starwars/form.html', context)


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


def request_log(request):
    requests = RequestLog.objects.order_by('id')[:10]
    context = {
        'requests': requests
    }
    return render(request, 'starwars/request_log.html', context)


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.POST['redirect'])
        else:
            context = {
                'message': 'LOGIN INCORRECT',
                'redirect': request.POST['redirect']
            }
            return render(request, 'starwars/login.html', context)
    else:
        context = {
            'redirect': request.GET['next']
        }

    return render(request, 'starwars/login.html', context)


def logout_form(request):
    logout(request)
    return redirect('index')