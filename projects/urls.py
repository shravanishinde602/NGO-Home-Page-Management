from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.projects_page, name="projects_page"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("dashboard/projects/", views.manage_projects, name="manage_projects"),
    path("dashboard/project-images/", views.manage_project_images, name="manage_project_images"),
]
