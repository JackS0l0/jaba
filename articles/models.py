from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
class Categories(models.Model):
    name=models.CharField('Title',max_length=200,unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class Articles (models.Model):
    name=models.CharField('Title', max_length=200,unique=True)
    category=models.ForeignKey(to=Categories,on_delete=models.CASCADE,verbose_name='Category')
    img=models.ImageField('Image',upload_to='archive')
    date=models.DateTimeField('Date',default=timezone.now)
    txt=RichTextField('Text',default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'