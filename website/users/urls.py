from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = "users"


urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    # path("logout/", auth_view.LogoutView.as_view(),name="logout",),
    path("logout/", views.logout_view, name='logout'),
]
