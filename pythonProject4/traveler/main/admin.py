from django.contrib import admin
from .models import Attraction
from .models import Comment
from modeltranslation.admin import TranslationAdmin

from django.contrib import admin
from .models import Attraction, Comment


class AttractionAdmin(TranslationAdmin):
    list_display = ['attraction', 'attraction_type', 'region']
    search_fields = ['attraction', 'region']
    # list_filter = ['attraction_type', 'region']
    # exclude = ['information']
    # readonly_fields = ['attraction', 'region']

admin.site.register(Attraction, AttractionAdmin)

class CommentAdmin(TranslationAdmin):
    list_display = ['user', 'subject', 'message']
    search_fields = ['user', 'subject']
    # list_filter = ['message']

admin.site.register(Comment, CommentAdmin)