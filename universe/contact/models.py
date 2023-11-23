from django.db import models

class Contact(models.Model):
    phone = models.CharField('Phone', max_length=50)
    address = models.TextField('Address', max_length=2000)
    mail = models.TextField('E-mail', max_length=2000)
    

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'


class Message(models.Model):
    mail = models.EmailField('E-mail', max_length=200)
    subject = models.CharField('Subject', max_length=200)
    text = models.TextField('Text',)


    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class SocialMedia(models.Model):
    
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)

    class Meta():
        verbose_name = 'Social media'
        verbose_name_plural = 'Social media'