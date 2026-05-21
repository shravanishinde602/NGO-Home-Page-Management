from django.contrib import messages
from django.shortcuts import redirect, render

from home.views import save_or_delete, staff_required

from .forms import CoreValueForm, ImpactStatisticForm, OurStoryForm, ProgramForm, TeamMemberForm
from .models import CoreValue, ImpactStatistic, OurStory, Program, TeamMember


def about_page(request):
    context = {
        "story": OurStory.objects.first(),
        "values": CoreValue.objects.filter(status=True),
        "programs": Program.objects.filter(status=True),
        "team_members": TeamMember.objects.filter(status=True),
        "impact_statistics": ImpactStatistic.objects.filter(status=True),
    }
    return render(request, "about.html", context)


@staff_required
def manage_story(request):
    instance = OurStory.objects.first()
    form = OurStoryForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "About story content saved successfully.")
        return redirect("manage_story")
    return render(request, "manage_story.html", {"form": form})


@staff_required
def manage_values(request):
    return save_or_delete(request, CoreValue, CoreValueForm, "manage_values.html", "Core Value", "manage_values")


@staff_required
def manage_programs(request):
    return save_or_delete(request, Program, ProgramForm, "manage_programs.html", "Program", "manage_programs")


@staff_required
def manage_team(request):
    return save_or_delete(request, TeamMember, TeamMemberForm, "manage_team.html", "Team Member", "manage_team")


@staff_required
def manage_about_impact(request):
    return save_or_delete(
        request,
        ImpactStatistic,
        ImpactStatisticForm,
        "manage_about_impact.html",
        "About Impact Statistic",
        "manage_about_impact",
    )
