import json
from django import forms
from django.db.models import F, Func
from django.db import models
from django.contrib.postgres.fields import ArrayField

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wazimap.models import DBTable, FieldTable
from wagtail.admin.forms import WagtailAdminModelForm
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    """
    HURUmap Home Page
    """
    intro = models.CharField(max_length=250)
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class StaticPage(Page):
    """
    HURUmap Static Pages such as about, privacy, etc
    """
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

CHART_TYPES = (
        ('', '-----------'),
        ('column', 'Column'),
        ('histogram', 'Histogram'),
        ('line', 'Line'),
        ('grouped_column', 'Grouped Column'),
        ('pie', 'Pie'),
    )

STAT_TYPES = (
       ('number', 'Number'),
       ('percentage', 'Percentage'),
    )

class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class CustomChartForm(WagtailAdminModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["table"].widget.attrs.update(
            {
                "data-fields": json.dumps(
                    list(FieldTable.objects.values("name", "fields"))
                )
            }
        )

        self.fields["fields"].choices = tuple(
            map(
                lambda x: (x, x),
                list(
                    set(
                        FieldTable.objects.annotate(
                            table_fields=Func(F("fields"), function="UNNEST")
                        ).values_list("table_fields", flat=True)
                    )
                ),
            )
        )

        self.fields["group_by"].choices = self.fields["fields"].choices

    table = CustomChoiceField(
        widget=forms.Select(attrs={"id": "chart-table", "data-fields": "{}"}),
        queryset=DBTable.objects.all(),
    )

    fields = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={"id": "chart-fields"})
    )

    chart_type = forms.ChoiceField(
        widget=forms.Select(attrs={"id": "chart-type"}),
        choices=CHART_TYPES
    )

    group_by = forms.ChoiceField(
        widget=forms.Select(attrs={"id": "group_by"}),
    )

    class Media:
        js = ("js/profile_chart.js",)


@register_snippet
class ChartSection(models.Model):
    name = models.CharField(default="Default Section", null=False, blank=False, unique=True, max_length=1024,
        help_text="Provide a unique name for profile section")

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return '{}'.format(self.name)

@register_snippet
class Chart(models.Model):
    table = models.ForeignKey(DBTable, on_delete=models.CASCADE)
    chart_type = models.CharField(max_length=32, null=False)
    fields = ArrayField(models.CharField(max_length=150, null=False, unique=True))
    title = models.CharField(max_length=500, null=True, blank=True, help_text="Descriptive title of this chart")
    source = models.CharField(max_length=500, null=True, blank=True, help_text="Data source")
    source_link = models.URLField(max_length=500, null=True, blank=True, help_text="Link to data source")
    stat_type = models.CharField(max_length=32, null=True, blank=True, choices=STAT_TYPES, help_text="Default is Number")
    group_by = models.CharField(max_length=120, null=True, blank=True)
    section = models.ForeignKey(ChartSection, on_delete=models.CASCADE, help_text="Select profile section where the chart belongs to")

    panels = [
        FieldPanel('table'),
        FieldPanel('fields'),
        FieldPanel('chart_type'),
        FieldPanel('title'),
        FieldPanel('section'),
        FieldPanel('source'),
        FieldPanel('source_link'),
        FieldPanel('stat_type'),
        FieldPanel('group_by'),
    ]
    base_form_class = CustomChartForm

    def __str__(self):
        return '%s Chart with field(s) %s' % (self.chart_type.capitalize(), (', '.join(self.fields)))

    def as_dict(self):
        return {
            'name': str(self),
            'title': self.title,
            'field': ','.join(self.fields),
            'stat_type': self.stat_type,
            'table_id': self.table.name,
            'chart_type': self.chart_type,
            'source': self.source,
            'source_link': self.source_link,
            'group_by': self.group_by,
            'section': str(self.section)
        }
