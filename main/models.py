from django.db import models
from ckeditor.fields import RichTextField
class About(models.Model):
    name=models.CharField('Name',max_length=200)
    txt=RichTextField('About me')
    img=models.URLField('Foto',default='',null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'About me'
        verbose_name_plural = 'About me'