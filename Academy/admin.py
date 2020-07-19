from django.contrib import admin
from .models import TeamType, Coach, Stuff, Player, Supporter, Team, TeamCoaches, Test, TestResults, Match, MatchSummary, DayName, Trainings

admin.site.register(TeamType)
admin.site.register(Coach)
admin.site.register(Stuff)
admin.site.register(Player)
admin.site.register(Supporter)
admin.site.register(Team)
admin.site.register(TeamCoaches)
admin.site.register(Test)
admin.site.register(TestResults)
admin.site.register(Match)
admin.site.register(MatchSummary)
admin.site.register(DayName)
admin.site.register(Trainings)
