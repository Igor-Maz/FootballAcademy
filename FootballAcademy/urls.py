"""FootballAcademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from Academy import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='url_index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    path('coach/', views.CoachListView.as_view(), name='url_coach'),
    path('coach/<int:pk>/', views.CoachDetailsView.as_view(), name="url_coach_details"),
    path('coach/update/<pk>/', views.CoachUpdateView.as_view(), name="url_coach_update"),
    path('coach/delete/<pk>/', views.CoachDeleteView.as_view(), name="url_coach_delete"),
    path('coach/add/', views.CoachAddView.as_view(), name='url_coach_add'),

    path('stuff/', views.StuffListView.as_view(), name='url_stuff'),
    path('stuff/<int:pk>/', views.StuffDetailsView.as_view(), name="url_stuff_details"),
    path('stuff/update/<pk>/', views.StuffUpdateView.as_view(), name="url_stuff_update"),
    path('stuff/delete/<pk>/', views.StuffDeleteView.as_view(), name="url_stuff_delete"),
    path('stuff/add/', views.StuffAddView.as_view(), name='url_stuff_add'),

    path('player/', views.PlayerListView.as_view(), name='url_player'),
    path('player/<int:pk>/', views.PlayerDetailsView.as_view(), name="url_player_details"),
    path('player/update/<pk>/', views.PlayerUpdateView.as_view(), name="url_player_update"),
    path('player/delete/<pk>/', views.PlayerDeleteView.as_view(), name="url_player_delete"),
    path('player/add/', views.PlayerAddView.as_view(), name='url_player_add'),

    path('team/', views.TeamListView.as_view(), name='url_team'),
    path('team/<int:pk>/', views.TeamDetailsView.as_view(), name="url_team_details"),
    path('team/update/<pk>/', views.TeamUpdateView.as_view(), name="url_team_update"),
    path('team/delete/<pk>/', views.TeamDeleteView.as_view(), name="url_team_delete"),
    path('team/add/', views.TeamAddView.as_view(), name='url_team_add'),

    path('supporter/', views.SupporterListView.as_view(), name='url_supporter'),
    path('supporter/<int:pk>/', views.SupporterDetailsView.as_view(), name="url_supporter_details"),
    path('supporter/update/<pk>/', views.SupporterUpdateView.as_view(), name="url_supporter_update"),
    path('supporter/delete/<pk>/', views.SupporterDeleteView.as_view(), name="url_supporter_delete"),
    path('supporter/add/', views.SupporterAddView.as_view(), name='url_supporter_add'),
]
