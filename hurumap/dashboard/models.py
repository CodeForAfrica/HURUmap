from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

class HomePage(Page):
    '''
    HURUmap Home Page
    '''
    intro = models.CharField(max_length=250)
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class StaticPage(Page):
    '''
    HURUmap Static Pages such as about, privacy, etc
    '''
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image"))
    ], null=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class BlogIndexPage(Page):
    """
    Blog Home Page
    """
    intro = models.CharField(max_length=250)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class BlogPostPage(Page):
    """
    Actual blog Post
    """
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image"))
    ], null=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

    promote_panels = [
        ImageChooserPanel('featured_image'),
    ]
