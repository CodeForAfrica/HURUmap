from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class DataIndicatorAuthor(models.Model):
    '''
    Data Indicator Author
    '''
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField()


class DataIndicator(models.Model):
    '''
    Data Indicator as referenced:
    https://datahelpdesk.worldbank.org/knowledgebase/articles/898599-api-indicator-queries
    '''
    author = models.ForeignKey(DataIndicatorAuthor,null=True,blank=True)
    author_code = models.CharField(max_length=255)
    author_data = JSONField()
    
    name = models.CharField(max_length=255)
    source = JSONField()
    source_note = models.TextField()
    topics = JSONField(default=[])


class DataIndicatorValue(models.Model):
    '''
    Data Indicator value
    '''

    indicator = models.ForeignKey(DataIndicator)
    author_data = JSONField()

    country = JSONField()
    date = models.CharField(max_length=255)
    decimal = models.IntegerField(null=True,blank=True)
    value = models.DecimalField(max_digits=36,decimal_places=15,null=True,blank=True)
