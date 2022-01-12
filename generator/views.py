from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def hello_word(request):
    return HttpResponse("Helo Word")

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html', {'name': 'Stev'})

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    lentgh = int(request.GET.get('lentgh', 10))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-_'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(lentgh):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})
