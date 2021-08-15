from django.core.checks import messages
from django.shortcuts import render
from .models import JokeCalls
import random

def chat_room(request):
    return render(request,'chat/room.html')

def joke_calls(request):
    calls=JokeCalls.objects.all()
    return render(request,'chat/calls.html',{'calls':calls})

def add_call(name):
    try:
        joke=JokeCalls.objects.get(name=name)
        joke.calls+=1
        joke.save()
    except JokeCalls.DoesNotExist:
        joke=JokeCalls.objects.create(name=name,calls=1)
        joke.save()
def respond_to_websockets(message):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  

    result_message = {
        'type': 'text'
    }
    if 'fat' in message:
        add_call('fat')
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message:
        add_call('dumb')
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message:
        add_call('stupid')
        result_message['text'] = random.choice(jokes['dumb'])
    return result_message
    