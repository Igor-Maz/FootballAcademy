from django import forms
from .models import Coach, Stuff, Player, Supporter, Team, Test, TestResults, Match, MatchSummary, Trainings

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'


class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = '__all__'


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class SupporterForm(forms.ModelForm):
    class Meta:
        model = Supporter
        fields = '__all__'


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResults
        fields = '__all__'


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'


class MatchSummaryForm(forms.ModelForm):
    class Meta:
        model = MatchSummary
        fields = '__all__'


class TrainingsForm(forms.ModelForm):
    class Meta:
        model = Trainings
        fields = '__all__'
