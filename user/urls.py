from django.urls import path
from . import views

urlpatterns = [
    path('all', views.show_users, name='show_users'),
    path('<int:user_id>', views.user_details, name='user_details'),
    path('new/', views.create_user, name='create_user'),
]