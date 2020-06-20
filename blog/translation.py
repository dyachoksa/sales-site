from modeltranslation.translator import TranslationOptions, register

from .models import Post


@register(Post)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", "content")
