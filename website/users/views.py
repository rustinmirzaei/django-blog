from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterationForm


def register(request):
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"Account created for {username}")
            return redirect("blog:home")
    else:
        form = UserRegisterationForm()

    return render(request, "users/register.html", {"form": form})


def profile(request):
    return render(request, "users/profile.html")