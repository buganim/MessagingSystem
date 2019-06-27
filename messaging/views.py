from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from datetime import datetime
from .models import Message

# Create your views here.


@csrf_exempt
def writeMessage(request):

    # Validate request being POST
    if request.method == "POST":

        # Get all required request fields
        try:
            username = request.GET['username']
            password = request.GET['password']
            receiver = request.GET['receiver']
            subject = request.GET['subject']
            content = request.GET['content']
        except:
            return HttpResponse("Missing Fields in request.", 400)

        # Authenticate user
        user = authenticate(
            username=username, password=password)
        receiver = User.objects.get(username=receiver)

        # Create Message for user
        if user is not None and receiver is not None:
            Message.objects.create(
                sender=username, receiver=receiver, subject=subject, content=content, creation_date=str(datetime.now())[:10])
            return HttpResponse("Message created", 200)
        else:
            return HttpResponse("Username or Password incorrect", 400)

    else:
        return HttpResponse("POST Request required", 400)


@csrf_exempt
def deleteMessage(request):

    # Validate request being POST
    if request.method == "POST":

        # Get all required request fields
        try:
            username = request.GET['username']
            password = request.GET['password']
            del_id = request.GET['id']
        except:
            return HttpResponse("Missing Fields in request.", 400)

         # Authenticate user
        user = authenticate(
            username=username, password=password)

        # Delete required message
        if user is not None and (Message.objects.get(id=del_id).sender == username or Message.objects.get(id=del_id).receiver == username):
            try:
                Message.objects.filter(id=del_id).delete()
                return HttpResponse("Message(id=%s) deleted." % del_id, 200)

            except:
                return HttpResponse("Message not found or doesn't belong to user.")

        else:
            return HttpResponse("Message not found or doesn't belong to user.")
    else:
        return HttpResponse("POST Request required", 400)


def readMessage(request):

    # Validate request being GET
    if request.method == "GET":

        # Get all required request fields
        try:
            username = request.GET['username']
            password = request.GET['password']
        except:
            return HttpResponse("Missing Fields in request.", 400)

        # Authenticate user
        user = authenticate(
            username=username, password=password)

        # Return a list of all the user's messages send/received
        if user is not None:
            for msg in Message.objects.all():
                if msg.receiver == username and msg.isRead == False:
                    msg.isRead = True
                    msg.save()
                    return HttpResponse(msg, 200)
                else:
                    return(HttpResponse(None))
        else:
            return HttpResponse("Username or Password incorrect", 400)
    else:
        return HttpResponse("GET Request required", 400)


def getAll(request):

    # Validate request being GET
    if request.method == "GET":
        all_messages = []

        # Get all required request fields
        try:
            username = request.GET['username']
            password = request.GET['password']
        except:
            return HttpResponse("Missing Fields in request.", 400)

        # Authenticate user
        user = authenticate(
            username=username, password=password)

        # Return a list of all the user's messages send/received
        if user is not None:
            for msg in Message.objects.all():
                if msg.sender == username or msg.receiver == username:
                    all_messages.append(msg)
            return HttpResponse(all_messages, 200)
        else:
            return HttpResponse("Username or Password incorrect", 400)
    else:
        return HttpResponse("GET Request required", 400)


def getUnread(request):

    # Validate request being GET
    if request.method == "GET":
        all_messages = []

        # Get all required request fields
        try:
            username = request.GET['username']
            password = request.GET['password']
        except:
            return HttpResponse("Missing Fields in request.", 400)

        # Authenticate user
        user = authenticate(
            username=username, password=password)

        # Return a list of all the user's unread received messages
        if user is not None:
            for msg in Message.objects.all():
                if msg.receiver == username and msg.isRead == False:
                    all_messages.append(msg)
            return HttpResponse(all_messages, 200)
        else:
            return HttpResponse("Username or Password incorrect", 400)
    else:
        return HttpResponse("GET Request required", 400)
