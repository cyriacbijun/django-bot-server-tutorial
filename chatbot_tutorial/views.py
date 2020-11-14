from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render
import spacy
nlp = spacy.load("en_core_web_sm")


def chat(request):
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    result_message = {
        'type': 'text'
    }
    message = message['text']
    words = message.split()
    if(len(words) == 1):
        message = "I'm " + message
    doc = nlp(message)
    flag = 0
    for ent in doc.ents:
        if(ent.label_ == "PERSON"):
            result_message['text'] = "Hello " + ent.text
            flag = 1
    if(flag == 0):
        result_message['text'] = "I don't know any responses for that. Please introduce yourself"

    return result_message
    