from django import forms
from django.contrib.auth.models import Group, User


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
        widgets = {
            'permissions': forms.CheckboxSelectMultiple()
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_permissions', 'groups', 'username']
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple(),
            'groups': forms.CheckboxSelectMultiple(),
        }
