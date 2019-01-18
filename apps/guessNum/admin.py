from django.contrib import admin

from apps.guessNum.models import NumberModel


class NumberModelAdmin(admin.ModelAdmin):
    pass



admin.site.register(NumberModel, NumberModelAdmin)