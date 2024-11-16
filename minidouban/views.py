# views.py
from django.shortcuts import render

def movie_info(request):
    return render(request, 'movie_info.html')
