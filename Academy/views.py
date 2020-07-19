from django import forms
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from .models import Coach, Stuff, Player, Supporter, Team, Test, TestResults, Match, MatchSummary, Trainings


class Index(View):
    def get(self, request):
        return render(request, 'index.html', {'app_version': '111.1 - można to nadpisać w konkretnym widoku'})


class CoachListView(ListView):
    model = Coach
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': Coach.objects.all(), 'category': 'coach', 'title': 'Trenerzy w akademii:'})
        return context


class CoachDetailsView(DetailView):
    model = Coach
    fields = '__all__'
    template_name = 'general_content.html'

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({Coach.objects.get(id=id)})
        return context


class CoachUpdateView(UpdateView):
    model = Coach
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/coach/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class CoachDeleteView(DeleteView):
    model = Coach
    template_name = 'delete.html'
    success_url = '/coach/'
    extra_context = {'return_url': '/coach/'}


class CoachAddView(CreateView):
    model = Coach
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/coach/'


class StuffListView(ListView):
    model = Stuff
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': Stuff.objects.all(), 'category': 'stuff', 'title': 'Kadra w akademii:'})
        return context


class StuffDetailsView(DetailView):
    model = Stuff
    fields = '__all__'
    template_name = 'general_content.html'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class StuffUpdateView(UpdateView):
    model = Stuff
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/stuff/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class StuffDeleteView(DeleteView):
    model = Stuff
    template_name = 'delete.html'
    success_url = '/stuff/'
    extra_context = {'return_url': '/stuff/'}


class StuffAddView(CreateView):
    model = Stuff
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/stuff/'


class PlayerListView(ListView):
    model = Player
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': Player.objects.all(), 'category': 'player', 'title': 'Piłkarze w akademii:'})
        return context


class PlayerDetailsView(DetailView):
    model = Player
    fields = '__all__'
    template_name = 'general_content.html'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class PlayerUpdateView(UpdateView):
    model = Player
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/player/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'delete.html'
    success_url = '/player/'
    extra_context = {'return_url': '/player/'}


class PlayerAddView(CreateView):
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


class TeamDetailsView(View):
    def get(self, request, id):
        team = Team.objects.get(id=id)
        coach = Coach.objects
        return render(request, 'team_details.html', {'team': team, })


class TeamUpdateView(UpdateView):
    model = Team
    fields = '__all__'
    widgets = {
        'players': forms.CheckboxSelectMultiple(),
        'stuff': forms.CheckboxSelectMultiple(),
        'coach': forms.CheckboxSelectMultiple()
    }
    template_name = 'general_content.html'
    success_url = '/team/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'delete.html'
    success_url = '/team/'
    extra_context = {'return_url': '/team/'}


class TeamAddView(CreateView):
    model = Team
    # form_class =
    fields = ['name', 'description', 'type', 'players']
    # exclude = ['coach', 'stuff']
    widgets = {
        'players': forms.CheckboxSelectMultiple()
    }
    template_name = 'general_content.html'
    success_url = '/team/'


class SupporterListView(ListView):
    model = Supporter
    template_name = 'objects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': Supporter.objects.all(), 'category': 'supporter', 'title': 'Kibice:'})
        return context


class SupporterDetailsView(DetailView):
    model = Supporter
    fields = '__all__'
    template_name = 'general_content.html'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class SupporterUpdateView(UpdateView):
    model = Supporter
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/supporter/'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class SupporterDeleteView(DeleteView):
    model = Supporter
    template_name = 'delete.html'
    success_url = '/supporter/'
    extra_context = {'return_url': '/supporter/'}


class SupporterAddView(CreateView):
    model = Supporter
    fields = '__all__'
    template_name = 'general_content.html'
    success_url = '/supporter/'
