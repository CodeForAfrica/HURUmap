from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

class DataIndicator(models.Model):
    '''
    Data Indicator as referenced:
    https://datahelpdesk.worldbank.org/knowledgebase/articles/898599-api-indicator-queries
    '''

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    source_id = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)
    source_note = models.TextField()
    topics = ArrayField(
        JSONField()
    )
