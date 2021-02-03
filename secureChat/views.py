from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .signForm import UserForm, LoginForm
from .models import PubKeyWithServer
import hashlib

def index(request):
    return render(request, 'secureChat/index.html', {})

def room(request, room_name):

    if(all(ord(c) <128 for c in room_name) and room_name.isalnum()):
        print("AA")
    else:
        return redirect("/")
    
    serverNameHash = hashlib.sha512(str(room_name).encode('utf-8')).hexdigest()
    PubKey=''

    if(PubKeyWithServer.objects.filter(serverNameHash=serverNameHash).exists()):
        PubKey=PubKeyWithServer.objects.get(serverNameHash=serverNameHash).pubKey
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



def error400(request, exception):
    data = {"message": "Bad Request "}
    return render(request,'secureChat/error.html', data)

def error403(request, exception):
    data = {"message": "Permission Denied"}
    return render(request,'secureChat/error.html', data)

def error404(request, exception):
    data = {"message": "Page Not Found"}
    return render(request,'secureChat/error.html', data)

def error500(request, exception):
    data = {"name": "Server Error"}
    return render(request,'secureChat/error.html', data)

