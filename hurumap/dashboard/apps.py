from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HURUmapDashboardConfig(AppConfig):
    name = 'hurumap.dashboard'
    label = 'hurumapdashboard'
    verbose_name = _("HURUmap Dashboard")
