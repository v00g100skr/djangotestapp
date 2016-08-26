import swapi

from django.core.cache import cache


def get_chars():
    chars = cache.get('chars')
    if not chars:
        swapi_characters = swapi.get_all("people")
        chars = {}
        for char in swapi_characters.items:
            char_index = swapi_characters.items.index(char)+1
            char_name = char.name.lower()
            chars[char_name] = char_index
            char_key = get_char_cache_key(char_name, char_index)
            cache.set(char_key, char)
        cache.set('chars', chars)

    return chars


def get_char(char_id):
    chars = get_chars()

    reversed_chars = {char_id: char_name for char_name, char_id in chars.iteritems()}
    char_name = reversed_chars[char_id]
    char_key = get_char_cache_key(char_name, char_id)

    char = cache.get(char_key)

    return char


def get_char_cache_key(name, id):
    # Cache key may contains characters that will cause errors if used with memcached
    return '%s_%s' % (name, id)