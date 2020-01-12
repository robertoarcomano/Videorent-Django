from django.shortcuts import render
from django.http import HttpResponse
from rent.models import Rent

def index(request):
    html = "<html><body><br><p align=center>"

    links = ["customer","article","rent"]
    for link in links:
        html += "<a href=" + link + ">" + link.upper() + "</a><br><br><br>"

    html = html + "</p></body></html>"
    return HttpResponse(html)
