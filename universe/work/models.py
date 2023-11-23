from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True, default='slug')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'


class WorkImage(models.Model):
    work = models.ForeignKey(
        'work.Work',
        on_delete = models.CASCADE,
        related_name= 'images'
        )
    image = models.ImageField(upload_to='work')


    class Meta:
        verbose_name = 'Work_image'
        verbose_name_plural = 'Work_images'



