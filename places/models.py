from django.db import models



class Place(models.Model):
    title = models.CharField(verbose_name='Название места', max_length=100, unique=True)
    short_description = models.TextField(verbose_name='Краткое описнаие', blank=True)
    long_description = models.TextField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')


    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(verbose_name='Название картинки', max_length=100)
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, verbose_name='Место', on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    def __str__(self):
        return self.title