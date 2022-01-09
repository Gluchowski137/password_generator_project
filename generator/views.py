from django.shortcuts import render
import random
import string
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):


    characters = string.ascii_lowercase

    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase
    if request.GET.get('special'):
        characters += string.punctuation
    if request.GET.get('numbers'):
        characters += string.digits



    length = int(request.GET.get('length',12))

    thepassword = ""

    for x in range(length):
        thepassword += random.choice(list(characters))

    return render(request,'generator/password.html' ,{'password':thepassword})

def info(request):
    return render(request,'generator/info.html')