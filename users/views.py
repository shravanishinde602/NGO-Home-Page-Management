from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from aboutus.models import CoreValue, ImpactStatistic, Program, TeamMember
from home.models import Banner, Initiative, NewsEvent, Partner, Statistic, Testimonial
from media_management.models import ImageGallery, MediaCoverage, PressRelease, Video
from projects.models import Project, ProjectImage

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
    counts = {
        "banners": Banner.objects.count(),
        "statistics": Statistic.objects.count(),
        "initiatives": Initiative.objects.count(),
        "news": NewsEvent.objects.count(),
        "testimonials": Testimonial.objects.count(),
        "partners": Partner.objects.count(),
        "about_values": CoreValue.objects.count(),
        "about_programs": Program.objects.count(),
        "about_team": TeamMember.objects.count(),
        "about_impact": ImpactStatistic.objects.count(),
        "projects": Project.objects.count(),
        "project_images": ProjectImage.objects.count(),
        "press_releases": PressRelease.objects.count(),
        "media_coverages": MediaCoverage.objects.count(),
        "gallery_images": ImageGallery.objects.count(),
        "videos": Video.objects.count(),
    }
    return render(request, "dashboard.html", {"counts": counts})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")
