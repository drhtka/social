# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
#from django.utils.text import slugify
from django.urls import reverse
from pytils.translit import slugify


class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='content_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=180, unique=True, verbose_name='Введите заголовок')
    slug = models.SlugField(max_length=220, db_index=True, verbose_name='slug')
    image = models.ImageField(upload_to='users/%Y/%d', blank=True, null=True, default='no_image_app_content.jpg', verbose_name='Загрузить изображение')
    entry = models.TextField(blank=True, verbose_name='Запись')
    created = models.DateTimeField(auto_now_add=True)
    # обратить внимание в settings стр 181 - AUTH_USER_MODEL = 'auth.User'
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contents_liked', blank=True)# related_name обращение модели
# переопределили метод save для автослуг
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)#чем заполнить, заголовком
            #super(Content, self).save(*args, **kwargs)#модель Content считается родителем, сохранить любые аргументы
            super(Content, self).save(*args, **kwargs)

    def get_absolute_url(self): # стандартная функция мы ее переопределяем
        return reverse('images:detail', kwargs={'id':self.id, 'slug':self.slug},)# social_content нэймспэйс в главном урл, detail  функция в представлении для детального просмотра
    # kwargs извлекать запись по id, ключ обратиться к id записи; 'slug'обратитьс к этим данным self.slug

    def __str__(self):
        return self.title
