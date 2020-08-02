from django import forms
from .models import Player, Team, Fan


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        exclude = ('profile',)
        widgets = {
            'favourite_players': forms.CheckboxSelectMultiple(),
            'favourite_teams': forms.CheckboxSelectMultiple(),
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        widgets = {
            'coach': forms.CheckboxSelectMultiple(choices='coaches'),
            'staff': forms.CheckboxSelectMultiple(choices='staff'),
            'players': forms.CheckboxSelectMultiple(),
        }
