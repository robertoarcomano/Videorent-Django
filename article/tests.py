from django.test import TestCase
from article.models import Article
import random
import math

class ArticleTestCase(TestCase):
    def test_create_check_delete(self):
        randomNumber = math.floor(1000*random.random())
        name = "testArticle_" + str(randomNumber)
        article = Article(name = name)
        article.save()
        article = Article.objects.filter(name = name)
        self.assertEqual(len(article),1)
        self.assertEqual(article[0].name,name)

        article.delete()
        article = Article.objects.filter(name = name)
        self.assertEqual(len(article),0)
