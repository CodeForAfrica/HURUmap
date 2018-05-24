from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HURUmapAdminConfig(AppConfig):
    name = 'hurumap.admin'
    label = 'hurumapadmin'
    verbose_name = _("HURUmap admin")
