from django.urls import path

from . import views

urlpatterns = [
    path("media/", views.media_page, name="media_page"),
    path("media/press-release/<int:pk>/", views.media_detail, name="media_detail"),
    path("dashboard/media/press-releases/", views.manage_press_releases, name="manage_press_releases"),
    path("dashboard/media/press-releases/<int:pk>/delete/", views.delete_press_release, name="delete_press_release"),
    path("dashboard/media/gallery/", views.manage_gallery, name="manage_gallery"),
    path("dashboard/media/gallery/<int:pk>/delete/", views.delete_gallery_image, name="delete_gallery_image"),
    path("dashboard/media/videos/", views.manage_videos, name="manage_videos"),
    path("dashboard/media/videos/<int:pk>/delete/", views.delete_video, name="delete_video"),
]
