Django doens t suport multilines on include tags 
i,e
```bash
    {% include 'partials/components/stat_card.html' with title="Total Students" 
    value=total_students icon="fa fa-users" 
    icon_color="text-success" %}
```

to by pass it, include int int you apps/apps.py
```bash
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yourapp'
    
    def ready(self):
        import re
        from django.template import base as template_base
        template_base.tag_re = re.compile(template_base.tag_re.pattern, re.DOTALL)
```