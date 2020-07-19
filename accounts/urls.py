from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('groups/', views.GroupsView.as_view(), name='groups'),
    path('updateGroup/<int:pk>/', views.UpdateGroupView.as_view(), name='updateGroup'),
    path('updateUser/<int:pk>/', views.UpdateUserView.as_view(), name='updateUser'),
]