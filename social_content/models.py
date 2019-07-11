# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='content_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=180, unique=True, verbose_name='Введите заголовок')
    slug = models.SlugField(max_length=220, db_index=True, verbose_name='slug')
    image = models.ImageField(upload_to='users/%Y/%d', blank=True, null=True, default='no_image_app_content.jpg', verbose_name='Загрузить изображение')
    entry = models.TextField(blank=True, verbose_name='Запись')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return set.title
