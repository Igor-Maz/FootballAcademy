from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from Accounts.forms import RegistrationForm, UpdateUserForm, ProfileRegistrationForm, ProfileForm, GroupForm, \
    UserUpdateFormAdmin


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.username = user.username
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.description = profile_form.cleaned_data['description']
            profile.year_of_birth = profile_form.cleaned_data['year_of_birth']
            profile.in_academy_since = profile_form.cleaned_data['in_academy_since']
            profile.role = profile_form.cleaned_data['role']

            profile_form.save()
            return redirect('login')

    else:
        form = RegistrationForm()
        profile_form = ProfileRegistrationForm()
        args = {'form': form, 'profile_form': profile_form}
        return render(request, 'signup.html', args)


def show_profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


class ProfileAddView(PermissionRequiredMixin, CreateView):
    permission_required = ['Accounts.add_profile']
    form_class = ProfileForm
    success_url = '/'
    template_name = 'general_content.html'


def update_profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('url_profile')

    else:
        form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        args = {'form': form, 'profile_form': profile_form}
        return render(request, 'profile_edit.html', args)


class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    success_url = '/'
    template_name = 'general_content.html'


class UsersView(View):

    def get(self, request):
        users = User.objects.all()
        return render(request, "users.html", {'users': users, 'title': 'Lista użytkowników'})


class UsersUpdateViewAdmin(PermissionRequiredMixin, UpdateView):
    permission_required = ['Accounts.change_user']
    form_class = UserUpdateFormAdmin
    model = User
    template_name = 'general_content.html'
    success_url = "/Accounts/users/"


class UsersDeleteViewAdmin(PermissionRequiredMixin, DeleteView):
    permission_required = ['Accounts.delete_user']
    model = User
    template_name = 'delete.html'
    success_url = '/Accounts/users/'
    extra_context = {'return_url': '/Accounts/users/'}


class GroupsView(View):

    def get(self, request):
        groups = Group.objects.all()
        return render(request, "groups.html", {'groups': groups, 'title': 'Grupy dostępów'})


class GroupAddView(PermissionRequiredMixin, CreateView):
    permission_required = ['Accounts.add_group']
    form_class = GroupForm
    model = Group
    success_url = '/Accounts/groups/'
    template_name = 'general_content.html'


class GroupUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['Accounts.change_group']
    form_class = GroupForm
    model = Group
    template_name = 'general_content.html'
    success_url = "/Accounts/groups"


class GroupDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['Accounts.delete_group']
    model = Group
    template_name = 'delete.html'
    success_url = '/Accounts/groups/'
    extra_context = {'return_url': '/Accounts/groups/'}
