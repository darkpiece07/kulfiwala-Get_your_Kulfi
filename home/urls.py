from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("signup", views.signupUser, name='signup'),
    path("profile", views.profileUser, name='profile'),
    path("about", views.about, name = 'about'),
    path("services", views.services, name = 'services'),
    path("contact", views.contact, name = "contact"),
    path("profile/update", views.updateProfileForm, name = "update_profile_form"),
    path("profile/update/done", views.updateProfile, name = "update_profile"),
    path("test/", views.debug),
    path("kulfi", views.kulfi, name="kulfi"),
    path("kulfi/vote", views.vote, name="vote")
]