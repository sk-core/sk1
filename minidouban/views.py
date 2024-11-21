# views.py
from django.shortcuts import render

from io import BytesIO
from django.http import HttpResponse

def movie_info(request):
    return render(request, 'movie_info.html')
