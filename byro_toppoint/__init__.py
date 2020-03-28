from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'byro_toppoint'
    verbose_name = 'byro Toppoint e.V plugin'

    class ByroPluginMeta:
        name = ugettext_lazy('byro Toppoint e.V plugin')
        author = 'Moritz Fago'
        description = ugettext_lazy('Short description')
        visible = True
        version = '0.0.1'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'byro_toppoint.PluginApp'
