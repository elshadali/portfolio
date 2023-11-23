from django.db import models


class About(models.Model):
    title = models.CharField('title', max_length=250)
    description = models.TextField('description')
    image = models.ImageField(upload_to='author')

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'
