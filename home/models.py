from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from .blocks import NewStreamFieldClass

class HomePage(Page):
    body = StreamField(NewStreamFieldClass, blank=True, use_json_field=True)
    

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]