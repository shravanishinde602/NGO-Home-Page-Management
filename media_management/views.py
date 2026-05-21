from urllib.parse import parse_qs, urlparse

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ImageGalleryForm, PressReleaseForm, VideoForm
from .models import ImageGallery, MediaCoverage, PressRelease, Video


def get_youtube_embed_url(url):
    parsed_url = urlparse(url)
    host = parsed_url.netloc.lower()

    if "youtu.be" in host:
        video_id = parsed_url.path.strip("/")
    elif "youtube.com" in host:
        video_id = parse_qs(parsed_url.query).get("v", [""])[0]
        if not video_id and "/embed/" in parsed_url.path:
            video_id = parsed_url.path.split("/embed/")[-1]
    else:
        return url

    return f"https://www.youtube.com/embed/{video_id}" if video_id else url


def media_page(request):
    videos = []
    for video in Video.objects.all():
        videos.append(
            {
                "description": video.description,
                "embed_url": get_youtube_embed_url(video.video_url),
                "uploaded_at": video.uploaded_at,
            }
        )

    context = {
        "press_releases": PressRelease.objects.all(),
        "media_coverages": MediaCoverage.objects.all(),
        "gallery_images": ImageGallery.objects.all(),
        "videos": videos,
    }
    return render(request, "media_management/media.html", context)


def media_detail(request, pk):
    press_release = get_object_or_404(PressRelease, pk=pk)
    return render(
        request,
        "media_management/media_detail.html",
        {"press_release": press_release},
    )


@staff_member_required
def manage_press_releases(request):
    form = PressReleaseForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Press release added successfully.")
        return redirect("manage_press_releases")

    return render(
        request,
        "media_management/manage_press_releases.html",
        {"form": form, "press_releases": PressRelease.objects.all()},
    )


@staff_member_required
def delete_press_release(request, pk):
    press_release = get_object_or_404(PressRelease, pk=pk)
    if request.method == "POST":
        press_release.delete()
        messages.success(request, "Press release deleted.")
    return redirect("manage_press_releases")


@staff_member_required
def manage_gallery(request):
    form = ImageGalleryForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Gallery image uploaded successfully.")
        return redirect("manage_gallery")

    return render(
        request,
        "media_management/manage_gallery.html",
        {"form": form, "gallery_images": ImageGallery.objects.all()},
    )


@staff_member_required
def delete_gallery_image(request, pk):
    gallery_image = get_object_or_404(ImageGallery, pk=pk)
    if request.method == "POST":
        gallery_image.delete()
        messages.success(request, "Gallery image deleted.")
    return redirect("manage_gallery")


@staff_member_required
def manage_videos(request):
    form = VideoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Video added successfully.")
        return redirect("manage_videos")

    videos = [
        {
            "item": video,
            "embed_url": get_youtube_embed_url(video.video_url),
        }
        for video in Video.objects.all()
    ]
    return render(
        request,
        "media_management/manage_videos.html",
        {"form": form, "videos": videos},
    )


@staff_member_required
def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        video.delete()
        messages.success(request, "Video deleted.")
    return redirect("manage_videos")
