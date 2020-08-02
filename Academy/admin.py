from django.contrib import admin
from .models import TeamType, Player, Team, Fan

admin.site.register(TeamType)
admin.site.register(Player)
admin.site.register(Fan)
admin.site.register(Team)
