from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Site under construction. This is the future page for mapgen.")

def get_svg(request, svg_id):
    return HttpResponse("Site under construction. congratz on getting here though!")