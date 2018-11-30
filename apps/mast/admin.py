from django.contrib import admin

from apps.mast.models import incidents


class incidentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'Time', 'islastest', 'sId', 'fId', 'reporter')


admin.site.register(incidents, incidentsAdmin)
