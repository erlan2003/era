from modeltranslation.translator import register, TranslationOptions
from .models import Attraction, Comment

@register(Attraction)
class AttractionTranslationOptions(TranslationOptions):
    fields = ('attraction', 'attraction_type', 'region', 'information')

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('attraction', 'subject', 'message')