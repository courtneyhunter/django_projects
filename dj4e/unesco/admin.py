from django.contrib import admin

# Register your models here.

from unesco.models import site, category, iso, region, states

admin.site.register(site)
admin.site.register(category)
admin.site.register(iso)
admin.site.register(region)
admin.site.register(states)
