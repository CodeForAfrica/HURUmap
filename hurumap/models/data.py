from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

from wazimap.models import Geography


class DataIndicatorPublisher(models.Model):
    '''
    Data Indicator Publisher
    '''
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class DataIndicator(models.Model):
    '''
    Data Indicator as referenced:
    https://datahelpdesk.worldbank.org/knowledgebase/articles/898599-api-indicator-queries
    '''
    publisher = models.ForeignKey(DataIndicatorPublisher,null=True,blank=True)
    publisher_code = models.CharField(max_length=255)
    publisher_data = JSONField()

    title = models.CharField(max_length=255, blank=True)
    
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    source = JSONField(blank=True)
    source_note = models.TextField(blank=True)
    topics = JSONField(blank=True,default=[])

    class Meta:
        ordering = ['publisher_code']

    def __str__(self):
        return self.name.encode('ascii', 'ignore')


class DataIndicatorValue(models.Model):
    '''
    Data Indicator value
    '''

    indicator = models.ForeignKey(DataIndicator, on_delete=models.CASCADE)
    geo = models.ForeignKey(Geography, on_delete=models.SET_NULL,blank=True,null=True)

    # What the publisher provides
    publisher_data = JSONField(blank=True)

    country = JSONField()
    date = models.CharField(max_length=255)
    decimal = models.IntegerField(blank=True,null=True)
    value = models.DecimalField(max_digits=36,decimal_places=15,blank=True,null=True)


class DataTopic(models.Model):
    '''
    A topic from which data indicators can be organised around
    '''
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    indicators = models.ManyToManyField(DataIndicator)
