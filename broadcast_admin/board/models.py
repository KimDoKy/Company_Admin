from django.db import models
from django.conf import settings
from django.urls import reverse

class Board(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='글쓴이')
    title = models.CharField(max_length=50, verbose_name='제목')
    content = models.TextField(verbose_name='본문')
    photo = models.ImageField(blank=True, verbose_name='이미지')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('board:post_detil', args=[self.id])

    def __str__(self):
        return f'{self.title}'
