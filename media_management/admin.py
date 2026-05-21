from django.contrib import admin

from .models import ImageGallery, MediaCoverage, PressRelease, Video


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "created_at")
    search_fields = ("title", "description")
    list_filter = ("release_date",)


@admin.register(MediaCoverage)
class MediaCoverageAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "created_at")
    search_fields = ("title", "description", "url")


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ("description", "uploaded_at")
    search_fields = ("description",)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("description", "video_url", "uploaded_at")
    search_fields = ("description", "video_url")
