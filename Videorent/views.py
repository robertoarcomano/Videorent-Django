from django.shortcuts import render
from django.http import HttpResponse
from rent.models import Rent

from article.models import Article
from customer.models import Customer

def index(request):
    html = "<html><body><br><p align=center>"

    links = ["init", "customer","article","rent"]
    for link in links:
        html += "<a href=" + link + ">" + link.upper() + "</a><br><br><br>"

    html = html + "</p></body></html>"
    return HttpResponse(html)

def init(request):
    html = "Initializing..."
    n_articles = 10
    n_customers = 10
    articles = Article.init(n_articles)
    customers = Customer.init(n_customers)
    Rent.init(articles, customers)
    return HttpResponse(html)
