from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def indexy(request):
    return HttpResponse("<h2>How about that?")