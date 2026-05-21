from django.urls import path

from . import views

urlpatterns = [
    path("about/", views.about_page, name="about_page"),
    path("dashboard/about/story/", views.manage_story, name="manage_story"),
    path("dashboard/about/values/", views.manage_values, name="manage_values"),
    path("dashboard/about/programs/", views.manage_programs, name="manage_programs"),
    path("dashboard/about/team/", views.manage_team, name="manage_team"),
    path("dashboard/about/impact/", views.manage_about_impact, name="manage_about_impact"),
]
