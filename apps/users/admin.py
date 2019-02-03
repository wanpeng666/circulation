from django.contrib import admin

from apps.users.models import Users


class usersAdmin(admin.ModelAdmin):
    pass



admin.site.register(Users, usersAdmin)