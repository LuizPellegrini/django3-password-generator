from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': '(asdfgçlkjh)12'})

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    length = int(request.GET.get('length', 12))
    
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
    if request.GET.get('numbers'):
        characters.extend('0123456789')
        
    if request.GET.get('special'):
        characters.extend('!@#$%&*()+=}{')
        
    thepassword = ''
    
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password' : thepassword})

def about(request):
    return render(request, 'generator/about.html')