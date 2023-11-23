from django.db import models

class Main(models.Model):
    image = models.ImageField(upload_to='main')

    class Meta:
        verbose_name = 'main'
        verbose_name_plural = 'main'
    