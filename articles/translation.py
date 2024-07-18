from modeltranslation.translator import TranslationOptions,register
from .models import Articles,Categories
@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('name', 'txt')
@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ['name']