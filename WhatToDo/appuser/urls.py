from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView


app_name = "user"


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    # path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]
