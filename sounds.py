import json


def get_sounds():
    with open("mapping.json", 'r', encoding="utf-8") as mapfile:
        fulljson = json.load(mapfile)
    
    return fulljson["mapping"]


def find_sound(name):
    for sound in get_sounds():
        if sound['name'] == name:
            return sound
    
    return None


def get_sound_info(sound):
    return sound['name'], sound['channel'], sound['note'] if 'note' in sound else None, sound['cc'] if 'cc' in sound else None, sound["group"]


def get_group(sound):
    return sound['group']
