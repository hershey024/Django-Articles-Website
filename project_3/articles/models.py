from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
    'auth.user',
    on_delete = models.CASCADE,
    default = 1,
    )
    photo = models.ImageField(upload_to="gallary", default='herseys.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
