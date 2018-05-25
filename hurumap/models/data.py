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
    author = models.ForeignKey(DataIndicatorAuthor,blank=True,null=True)
    original = JSONField()

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    source_id = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)
    source_note = models.TextField()
    topics = ArrayField(
        JSONField()
    )

