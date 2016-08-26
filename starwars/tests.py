from django.test import TestCase

from .models import Characters


class CharactersTests(TestCase):

    def test_add(self):
        name = 'test name'
        height = 197
        mass = None
        hair_color = 'brown'
        skin_color = 'black'
        eye_color = 'blue'
        birth_year = 1234
        gender = 'male'

        new_character = Characters(name=name,
                                   height=height,
                                   mass=mass,
                                   hair_color=hair_color,
                                   skin_color=skin_color,
                                   eye_color=eye_color,
                                   birth_year=birth_year,
                                   gender=gender)


