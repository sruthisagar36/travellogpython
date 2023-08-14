from django.contrib import admin
from django.db.models import Model

from .models import Place, team

admin.site.register(Place)
admin.site.register(team)

