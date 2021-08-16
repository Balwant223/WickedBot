from django.core.checks import messages
from django.shortcuts import render
from .models import User
import random

def chat_room(request):
    room_id=random.randint(1000,10000)
    return render(request,'chat/room.html',{'room_id':room_id})

def joke_calls(request):
    users=User.objects.all()
    jokes={'fat':0,'dumb':0,'stupid':0}
    for u in users:
        jokes['fat']=jokes['fat']+u.f_joke
        jokes['stupid']=jokes['stupid']+u.s_joke
        jokes['dumb']=jokes['dumb']+u.d_joke
    return render(request,'chat/calls.html',{'users':users,'jokes':jokes})

def add_user(name,type):
    try:
        user=User.objects.get(name=name)
        if type=='f_type':
            user.f_joke+=1
            user.save()
        elif type=='d_type':
            user.d_joke+=1
            user.save()
        else:
            user.s_joke+=1
            user.save()
    except User.DoesNotExist:
        user=User.objects.create(name=name)
        user.save()

def respond_to_websockets(message,user):
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
        add_user(user,'f_type')
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message:
        add_user(user,'s_type')
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message:
        add_user(user,'d_type')
        result_message['text'] = random.choice(jokes['dumb'])
    else:
        result_message['text']='Hii {},I am a WickedBot. Sometimes people hate me but if you want to listen to a some Dumb,Stupid,Fat jokes then press below buttons '.format(user)

    return result_message
    