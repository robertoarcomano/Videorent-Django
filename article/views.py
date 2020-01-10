from django.shortcuts import render
from article.models import Article

def index(request):
    return render(request,
        'article/index.html',
        {
            'title': 'Article',
            'bodystart': 'Article',
            'articles': Article.objects.all(),
            'bodystop': 'bodystop',
        }
    )
