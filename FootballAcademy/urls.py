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
from django.conf.urls import include
from Academy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/', views.AboutUs.as_view(), name='url_aboutus'),
    path('', views.Index.as_view(), name='url_index'),
    path('Accounts/', include('django.contrib.auth.urls')),
    path('Accounts/', include('Accounts.urls')),

    path('coach/', views.CoachListView.as_view(), name='url_coach'),
    path('coach/<int:id>/', views.show_coach, name="url_coach_details"),
    path('coach/update/<pk>/', views.CoachUpdateView.as_view(), name="url_coach_update"),
    path('coach/delete/<pk>/', views.CoachDeleteView.as_view(), name="url_coach_delete"),

    path('staff/', views.StaffListView.as_view(), name='url_staff'),
    path('staff/<int:id>/', views.show_staff, name="url_staff_details"),
    path('staff/update/<pk>/', views.StaffUpdateView.as_view(), name="url_staff_update"),
    path('staff/delete/<pk>/', views.StaffDeleteView.as_view(), name="url_staff_delete"),

    path('player/', views.PlayerListView.as_view(), name='url_player'),
    path('player/<int:id>/', views.show_player, name="url_player_details"),
    path('player/update/<pk>/', views.PlayerUpdateView.as_view(), name="url_player_update"),
    path('player/delete/<pk>/', views.PlayerDeleteView.as_view(), name="url_player_delete"),
    path('player/add/', views.PlayerAddView.as_view(), name='url_player_add'),

    path('team/', views.TeamListView.as_view(), name='url_team'),
    path('team/<int:id>/', views.show_team, name="url_team_details"),
    path('team/update/<pk>/', views.TeamUpdateView.as_view(), name="url_team_update"),
    path('team/delete/<pk>/', views.TeamDeleteView.as_view(), name="url_team_delete"),
    path('team/add/', views.TeamAddView.as_view(), name='url_team_add'),

    path('fan/', views.FanListView.as_view(), name='url_fan'),
    path('fan/<int:id>/', views.show_fan, name="url_fan_details"),
    path('fan/update/<pk>/', views.FanUpdateView.as_view(), name="url_fan_update"),
    path('fan/delete/<pk>/', views.FanDeleteView.as_view(), name="url_fan_delete"),
    path('fan/add/', views.FanAddView.as_view(), name='url_fan_add'),
]
