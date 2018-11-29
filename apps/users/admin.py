from django.contrib import admin

from apps.users.models import User


class userAdmin(admin.ModelAdmin):
    pass



admin.site.register(User, userAdmin)