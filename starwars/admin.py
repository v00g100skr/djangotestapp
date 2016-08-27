from django.contrib import admin

from .models import Characters, CharactersLog, RequestLog


@admin.register(Characters)
class CharactersAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'mass', 'hair_color',
                    'skin_color', 'eye_color', 'birth_year', 'gender', 'pic')
    search_fields = ['name']


@admin.register(CharactersLog)
class CharactersLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'character_id', 'date')
    list_filter = ('action',)

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('scheme', 'path', 'method', 'code', 'status', 'date')
    list_filter = ('scheme', 'method', 'code', 'status')