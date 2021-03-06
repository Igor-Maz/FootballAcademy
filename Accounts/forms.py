from django import forms
from django.contrib.auth.models import User, Group
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
    last_name = forms.CharField(max_length=150, required=True,
                                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']


class UserUpdateFormAdmin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'groups']
        widgets = {
            'groups': forms.CheckboxSelectMultiple(),
        }


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'salary', 'username', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'salary']


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
        widgets = {
            'permissions': forms.CheckboxSelectMultiple()
        }
