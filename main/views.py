from django.shortcuts import render
from articles.models import Categories,Articles
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from .models import About
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
def home(request):
    data={
        'title':'JaBa',
        'categories':Categories.objects.all().order_by('name'),
        'categoriesWithOutTemplates': Categories.objects.all().order_by('name'),
        'articles':Articles.objects.all().order_by('-date')[4:10],
        'articles_in_right':Articles.objects.all().order_by('-date')[10:15],
        'first_article': Articles.objects.all().order_by('-date')[0:1],  
        'second_article': Articles.objects.all().order_by('-date')[1:2],
        'third_article': Articles.objects.all().order_by('-date')[2:3], 
        'fourth_article': Articles.objects.all().order_by('-date')[3:4],
    }
    return render(request,'index.html',data)
def about(request):
    data={
        'title': 'JaBa - About',
        'about': About.objects.all(),
    }
    return render(request, 'about.html',data)