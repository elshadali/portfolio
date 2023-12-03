from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True, default='slug')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='works', default='defaultwork.png')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'


