from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from main import views as mainviews
from articles import views as articlesViews
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',mainviews.home,name='homepage'),
    path('article/<int:pk>',articlesViews.ArticleDetail.as_view(),name='articlepage')
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", mainviews.set_language, name="set-language"),
]