from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.CharField(max_length=200, verbose_name='Изображение')
    release_date = models.CharField(max_length=10, verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=255, verbose_name='URL')
