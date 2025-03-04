from django.urls import path
from .views import IndexView, ProfileView, TaskCreateView

app_name = 'home'


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
]
