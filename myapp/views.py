from django.shortcuts import render
from django.http import JsonResponse
from .chatbt import chatbt

def home(request):
    return render(request, "index.html")

def get_bot_response(request):
    userText = request.GET.get('msg')
    response = str(chatbt.get_response(userText))
    return JsonResponse({'response': response})
