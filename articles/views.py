from typing import Any
from django.shortcuts import render
from .models import Categories,Articles
from django.views.generic import DetailView
class ArticleDetail(DetailView):
    model = Articles
    template_name = 'post.html'
    context_object_name = 'articles'
    def get_context_data(self, **kwargs):
        data=super(ArticleDetail,self).get_context_data()
        data['title']='Title'
        return data