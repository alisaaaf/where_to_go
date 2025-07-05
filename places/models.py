from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Название места', max_length=100, unique=True)
    short_description = models.TextField(verbose_name='Краткое описнаие', blank=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, verbose_name='Место', on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    position = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True,)

    def __str__(self):
        return f'{self.position} {self.place}'

    class Meta:
        ordering = ["position",]

