from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import views as auth_view
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterationForm


def register(request):
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"Account created for {username}")
            return redirect("users:login")
    else:
        form = UserRegisterationForm()

    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "users/profile.html")

def logout_view(request):
    login_url = reverse('users:login')
    msg = mark_safe(f"""Logut success. <a href="{login_url}">Login</a> again""")
    messages.success(request, f"{msg}")
    logout(request)
    return redirect("blog:home")


