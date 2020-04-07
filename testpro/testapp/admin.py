from django.contrib import admin
from testapp.models import players
# Register your models here.
class register_players(admin.ModelAdmin):
    list_display=["name","rank","no_matches","address"]
admin.site.register(players,register_players)
