from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_home, name="main_home"),
    path("dashboard/", views.admin_dashboard, name="dashboard"),
    path("dashboard/banners/", views.manage_banners, name="manage_banner"),
    path("dashboard/vision-mission/", views.manage_vision_mission, name="manage_vision_mission"),
    path("dashboard/statistics/", views.manage_statistics, name="manage_statistics"),
    path("dashboard/initiatives/", views.manage_initiatives, name="manage_initiatives"),
    path("dashboard/news/", views.manage_news, name="manage_news"),
    path("dashboard/testimonials/", views.manage_testimonials, name="manage_testimonials"),
    path("dashboard/partners/", views.manage_partners, name="manage_partners"),
]
