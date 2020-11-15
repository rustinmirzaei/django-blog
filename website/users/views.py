from django.shortcuts import render

from .forms import UserRegisterationForm


def register(request):
    form = UserRegisterationForm()

    return render(request, "users/register.html", {"form": form})
