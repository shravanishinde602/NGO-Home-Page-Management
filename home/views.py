from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    BannerForm,
    InitiativeForm,
    NewsEventForm,
    PartnerForm,
    StatisticForm,
    TestimonialForm,
    VisionMissionForm,
)
from .models import Banner, Initiative, NewsEvent, Partner, Statistic, Testimonial, VisionMission
from aboutus.models import CoreValue, ImpactStatistic, OurStory, Program, TeamMember


def main_home(request):
    context = {
        "banners": Banner.objects.filter(status=True),
        "vision_mission": VisionMission.objects.first(),
        "statistics": Statistic.objects.filter(status=True),
        "initiatives": Initiative.objects.filter(status=True),
        "news_events": NewsEvent.objects.filter(status=True)[:3],
        "testimonials": Testimonial.objects.filter(status=True),
        "partners": Partner.objects.filter(status=True),
    }
    return render(request, "main_home.html", context)


def staff_required(view_func):
    decorated_view = user_passes_test(lambda user: user.is_staff, login_url="login")(view_func)
    return login_required(decorated_view)


@staff_required
def admin_dashboard(request):
    counts = {
        "banners": Banner.objects.count(),
        "statistics": Statistic.objects.count(),
        "initiatives": Initiative.objects.count(),
        "news": NewsEvent.objects.count(),
        "testimonials": Testimonial.objects.count(),
        "partners": Partner.objects.count(),
        "about_story": OurStory.objects.count(),
        "about_values": CoreValue.objects.count(),
        "about_programs": Program.objects.count(),
        "about_team": TeamMember.objects.count(),
        "about_impact": ImpactStatistic.objects.count(),
    }
    return render(request, "dashboard.html", {"counts": counts})


def save_or_delete(request, model, form_class, template_name, title, redirect_name):
    item_id = request.GET.get("edit")
    instance = get_object_or_404(model, pk=item_id) if item_id else None

    if request.method == "POST":
        if "delete_id" in request.POST:
            get_object_or_404(model, pk=request.POST["delete_id"]).delete()
            messages.success(request, f"{title} deleted successfully.")
            return redirect(redirect_name)

        instance_id = request.POST.get("instance_id")
        instance = get_object_or_404(model, pk=instance_id) if instance_id else None
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, f"{title} saved successfully.")
            return redirect(redirect_name)
    else:
        form = form_class(instance=instance)

    return render(
        request,
        template_name,
        {
            "form": form,
            "items": model.objects.all(),
            "editing": instance,
            "page_title": f"Manage {title}",
        },
    )


@staff_required
def manage_banners(request):
    return save_or_delete(request, Banner, BannerForm, "manage_banner.html", "Banner", "manage_banner")


@staff_required
def manage_vision_mission(request):
    instance = VisionMission.objects.first()
    form = VisionMissionForm(request.POST or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Vision and mission updated successfully.")
        return redirect("manage_vision_mission")
    return render(request, "manage_vision_mission.html", {"form": form})


@staff_required
def manage_statistics(request):
    return save_or_delete(request, Statistic, StatisticForm, "manage_statistics.html", "Statistic", "manage_statistics")


@staff_required
def manage_initiatives(request):
    return save_or_delete(request, Initiative, InitiativeForm, "manage_initiatives.html", "Initiative", "manage_initiatives")


@staff_required
def manage_news(request):
    return save_or_delete(request, NewsEvent, NewsEventForm, "manage_news.html", "News/Event", "manage_news")


@staff_required
def manage_testimonials(request):
    return save_or_delete(request, Testimonial, TestimonialForm, "manage_testimonials.html", "Testimonial", "manage_testimonials")


@staff_required
def manage_partners(request):
    return save_or_delete(request, Partner, PartnerForm, "manage_partners.html", "Partner", "manage_partners")
