from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

from wazimap.models import Geography


class DataIndicatorPublisher(models.Model):
    """
    Data Indicator Publisher
    """
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class DataIndicator(models.Model):
    """
    Data Indicator
    https://github.com/TakwimuAfrica/TAKWIMU/blob/develop/DATA.md#data-indicator-schema
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # Data Values
    # -----------

    # Publisher of the data values, the code they use the data Indicator, and the data as they've published it
    publisher = models.ForeignKey(DataIndicatorPublisher,null=True,blank=True)
    publisher_code = models.CharField(max_length=255, blank=True)
    publisher_data = JSONField(blank=True, null=True)
    '''
    publisher_data: JSON Structure (WIP):

    {
        'type': 'csv',
        'url_original': 'https://data.worldbank.org/...'        # (Optional) Url to the original source of the data values.
        'url_local': '/data/{data_indicator.id}/some-name.csv'  # Location of where we've stored this locally.
    }
    '''

    # TODO: Attributes to be used to process the publisher_data into data_values
    process_prefs = JSONField(blank=True, null=True)
    '''
    process_prefs: JSON Structure (WIP)

    {}
    '''

    # Actual data values formatted for our purposes
    # NOTE: This is uploaded on CMS for now in CSV and transformed into a JSON
    # Question: Do we need any of the SQL functionality on these?
    # Question: If we already know from process_prefs how to manipulate the data, do we need to store the processed data?
    # TODO: Update the documentation with default structure needed.
    data_values = JSONField(blank=True, null=True)
    '''
    data_values: JSON Structure (WIP):

    {
        '<geo_code>': {
            'male': 50,
            'female': 50
        }
    }
    '''

    # Visualisation / Views
    # ---------------------

    view = JSONField(blank=True, null=True)
    '''
    view JSON Structure (WIP):

    {
        'type': 'chart.pie',  # Visualisation type
        'prefs': {            # Settings / preference to be used to visualise the data
            'data': [         # Data points to include in the chart
                'female',
                'male'
            ],
            'columns': {      # Mapping the columns from data_values
                'total': 'total'
            }
        }
    }
    '''

    class Meta:
        ordering = ['publisher_code']

    def __str__(self):
        return self.title.encode('ascii', 'ignore')


class DataTopic(models.Model):
    """
    A topic from which data indicators can be organised around
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    indicators = models.ManyToManyField(DataIndicator)
