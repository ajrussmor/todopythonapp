from django.contrib import admin
from .models import Todotab


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todotab, TodoAdmin)
