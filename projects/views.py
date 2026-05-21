from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from home.views import save_or_delete, staff_required

from .forms import ProjectForm, ProjectImageForm
from .models import Project, ProjectImage


def projects_page(request):
    selected_status = request.GET.get("status", "all")
    selected_category = request.GET.get("category", "all")
    projects = Project.objects.filter(status_active=True)

    if selected_status in [choice[0] for choice in Project.STATUS_CHOICES]:
        projects = projects.filter(status=selected_status)
    if selected_category in [choice[0] for choice in Project.CATEGORY_CHOICES]:
        projects = projects.filter(category=selected_category)

    context = {
        "projects": projects,
        "selected_status": selected_status,
        "selected_category": selected_category,
        "status_choices": Project.STATUS_CHOICES,
        "category_choices": Project.CATEGORY_CHOICES,
        "featured_stats": {
            "people_helped": sum(project.people_helped for project in Project.objects.filter(status_active=True)),
            "volunteers": sum(project.volunteers_engaged for project in Project.objects.filter(status_active=True)),
            "funds": sum(project.funds_raised for project in Project.objects.filter(status_active=True)),
        },
    }
    return render(request, "projects.html", context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id, status_active=True)
    related_projects = Project.objects.filter(status_active=True, category=project.category).exclude(pk=project.pk)[:3]
    return render(
        request,
        "project_detail.html",
        {"project": project, "gallery_images": project.gallery_images.all(), "related_projects": related_projects},
    )


@staff_required
def manage_projects(request):
    return save_or_delete(request, Project, ProjectForm, "manage_projects.html", "Project", "manage_projects")


@staff_required
def manage_project_images(request):
    return save_or_delete(
        request,
        ProjectImage,
        ProjectImageForm,
        "manage_project_images.html",
        "Project Image",
        "manage_project_images",
    )
