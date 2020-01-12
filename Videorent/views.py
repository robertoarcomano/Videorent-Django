from django.shortcuts import render
from django.http import HttpResponse
from rent.models import Rent
from article.models import Article
from customer.models import Customer
import time
import math

def index(request):
    html = "<html><body><br><p align=center>"

    links = ["init", "customer","article","rent"]
    for link in links:
        html += "<a href=" + link + ">" + link.upper() + "</a><br><br><br>"

    html = html + "</p></body></html>"
    return HttpResponse(html)

def init(request):
    def getSpeed(n,start,stop):
        return str(math.floor(n/(stop-start)))
    html = ""
    n_articles = 1000
    n_customers = 1000

    start = time.time()
    articles = Article.init(n_articles)
    stop = time.time()
    html += getSpeed(n_articles,start,stop) + " articles/s"
    html += "<br><br>"

    start = time.time()
    customers = Customer.init(n_customers)
    stop = time.time()
    html += getSpeed(n_customers,start,stop) + " customers/s"
    html += "<br><br>"

    start = time.time()
    Rent.init(articles, customers)
    stop = time.time()
    html += getSpeed(n_articles * n_customers,start,stop) + " rents/s"

    return HttpResponse(html)
