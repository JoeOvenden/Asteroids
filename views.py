from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "asteroids/index.html")

def highscores(request):
    return render(request, "asteroids/highscores.html")