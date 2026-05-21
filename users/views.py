from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistrationForm


def main_home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "main_home.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect("login")

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("dashboard")
        logout(request)
        messages.info(request, "Please log in with an admin or staff account.")
        return redirect("login")

    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        if user.is_staff:
            messages.success(request, "Welcome back.")
            return redirect("dashboard")
        logout(request)
        messages.error(request, "Only admin or staff users can access the dashboard.")
        return redirect("login")

    return render(request, "login.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")
