from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .forms import TeamForm
from .models import Player, Team, Fan
from Accounts.models import Profile


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutUs(View):
    def get(self, request):
        return render(request, 'about.html')


class CoachListView(ListView):
    model = Profile
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'object_list': Profile.objects.filter(role=1), 'category': 'coach', 'title': 'Trenerzy w akademii:'})
        return context


def show_coach(request, id):
    profile = Profile.objects.get(pk=id)
    teams = Team.objects.filter(coach=id)
    args = {'profile': profile, 'teams': teams, 'category': 'coach', 'title': 'Trener'}
    return render(request, 'individual_view.html', args)


class CoachUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['Accounts.change_profile']
    model = Profile
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/coach/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class CoachDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['Accounts.delete_profile']
    model = Profile
    template_name = 'delete.html'
    success_url = '/coach/'
    extra_context = {'return_url': '/coach/'}


class StaffListView(ListView):
    model = Profile
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'object_list': Profile.objects.filter(role=2), 'category': 'staff', 'title': 'Kadra w akademii:'})
        return context


def show_staff(request, id):
    profile = Profile.objects.get(pk=id)
    teams = Team.objects.filter(staff=id)
    args = {'profile': profile, 'teams': teams, 'category': 'staff', 'title': 'Pacownik klubu'}
    return render(request, 'individual_view.html', args)


class StaffUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['Accounts.change_profile']
    model = Profile
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/staff/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class StaffDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['Accounts.delete_profile']
    model = Profile
    template_name = 'delete.html'
    success_url = '/staff/'
    extra_context = {'return_url': '/staff/'}


class PlayerListView(ListView):
    model = Player
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': Player.objects.all(), 'category': 'player', 'title': 'Piłkarze w akademii:'})
        return context


def show_player(request, id):
    player = Player.objects.get(pk=id)
    profile = player.profile
    teams = Team.objects.filter(players=id)
    args = {'player': player, 'profile': profile, 'teams': teams, 'category': 'player', 'title': 'Zawodnik'}
    return render(request, 'player_view.html', args)


class PlayerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['Academy.change_player']
    model = Player
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/player/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class PlayerDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['Academy.delete_player']
    model = Player
    template_name = 'delete.html'
    success_url = '/player/'
    extra_context = {'return_url': '/player/'}


class PlayerAddView(PermissionRequiredMixin, CreateView):
    permission_required = ['Academy.add_player']
    model = Player
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/player/'


class TeamListView(ListView):
    model = Team
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': Team.objects.all(), 'category': 'team', 'title': 'Zespoły w akademii:'})
        return context


def show_team(request, id):
    team = Team.objects.get(pk=id)
    coaches = Profile.objects.filter(Coach=id)
    staffs = Profile.objects.filter(Staff=id)
    players = Player.objects.filter(team=id)
    args = {'team': team, 'coaches': coaches, 'staffs': staffs, 'players': players, 'category': 'team',
            'title': 'Zespół'}
    return render(request, 'team_view.html', args)


class TeamUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['Academy.change_team']
    model = Team
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/team/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class TeamDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['Academy.delete_team']
    model = Team
    template_name = 'delete.html'
    success_url = '/team/'
    extra_context = {'return_url': '/team/'}


class TeamAddView(PermissionRequiredMixin, CreateView):
    permission_required = ['Academy.add_team']
    form_class = TeamForm
    coaches = Profile.objects.filter(role=1)
    staffs = Profile.objects.filter(role=2)
    template_name = 'general_content.html'
    success_url = '/team/'


class FanListView(ListView):
    model = Fan
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': Fan.objects.all(), 'category': 'fan', 'title': 'Kibice:'})
        return context


def show_fan(request, id):
    fan = Fan.objects.get(pk=id)
    profile = fan.profile
    args = {'fan': fan, 'profile': profile, 'category': 'fun', 'title': 'Kibic'}
    return render(request, 'fan_view.html', args)


class FanUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['Academy.change_fan']
    model = Fan
    fields = ['favourite_teams', 'favourite_players']
    template_name = 'general_content.html'
    success_url = '/fan/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class FanDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['Academy.delete_fan']
    model = Fan
    template_name = 'delete.html'
    success_url = '/fan/'
    extra_context = {'return_url': '/fan/'}


class FanAddView(PermissionRequiredMixin, CreateView):
    permission_required = ['Academy.add_fan']
    model = Fan
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/fan/'
