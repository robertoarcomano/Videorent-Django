from django.db import models

class Article(models.Model):
    name = models.CharField("Name", max_length=30)
    def init(N):
        articles = Article.objects.filter(name__contains='Article_')
        articles.delete()
        articles = []
        for i in range(1,N+1):
            article = Article(name="Article_"+str(i))
            article.save()
            articles.append(article)
        return articles
