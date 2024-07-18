from modeltranslation.translator import TranslationOptions,register
from .models import About
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ['name','txt']