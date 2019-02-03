from django.contrib import admin

from apps.guessNum.models import GameNumberModel


class NumberModelAdmin(admin.ModelAdmin):
    pass



admin.site.register(GameNumberModel, NumberModelAdmin)