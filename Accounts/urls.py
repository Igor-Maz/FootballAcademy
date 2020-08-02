from django.urls import path
from Accounts import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('users/', views.UsersView.as_view(), name='ulr_users'),
    path('users/update/<int:pk>/', views.UsersUpdateViewAdmin.as_view(), name='url_users_update_admin'),
    path('users/delete/<int:pk>/', views.UsersDeleteViewAdmin.as_view(), name='url_users_delete_admin'),
    path('profile/', views.show_profile, name='url_profile'),
    path('profile/update/', views.update_profile, name='url_profile_update'),
    path('profile/add', views.ProfileAddView.as_view(), name='url_profile_add'),
    path('groups/', views.GroupsView.as_view(), name='ulr_groups'),
    path('groups/update/<int:pk>/', views.GroupUpdateView.as_view(), name='url_groups_update'),
    path('groups/add', views.GroupAddView.as_view(), name='url_groups_add'),
    path('groups/delete/<pk>', views.GroupDeleteView.as_view(), name='url_groups_delete')
]