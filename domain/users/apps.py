from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'domain.users'

    def ready(self):
        import re
        from django.template import base as template_base
        template_base.tag_re = re.compile(template_base.tag_re.pattern, re.DOTALL)