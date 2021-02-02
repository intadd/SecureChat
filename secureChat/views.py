from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .signForm import UserForm, LoginForm
from django.contrib.auth import login, authenticate
from .models import PubKeyWithServer
import hashlib
import urllib.parse

def index(request):
    return render(request, 'secureChat/index.html', {})

def room(request, room_name):


    print(room_name.isalnum())
    if(not room_name.isalnum()):
        return redirect("/")
    
    serverNameHash = hashlib.sha512(str(room_name).encode('utf-8')).hexdigest()
    PubKey=''

    if(PubKeyWithServer.objects.filter(serverNameHash=serverNameHash).exists()):
        PubKey=PubKeyWithServer.objects.get(serverNameHash=serverNameHash).pubKey
    room_name=urllib.parse.quote_plus(room_name)
    return render(request, 'secureChat/room.html', {
        'roomName': room_name,
        'pubKey': PubKey,
    })


def apiCreateServer(request):
    if(request.POST.get('serverName',False) and  request.POST.get("pubKey",False)):
        roomName=request.POST.get("serverName")
        pubKey=request.POST.get("pubKey")
        serverNameHash = hashlib.sha512(str(roomName).encode('utf-8')).hexdigest()
        
        if(not PubKeyWithServer.objects.filter(serverNameHash=serverNameHash).exists()):
            PubKeyWithServer.objects.create(pubKey=pubKey,serverNameHash=serverNameHash)



    return render(request, 'secureChat/index.html', {})

