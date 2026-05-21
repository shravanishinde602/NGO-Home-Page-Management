from django import forms

from .models import ImageGallery, PressRelease, Video


class PressReleaseForm(forms.ModelForm):
    class Meta:
        model = PressRelease
        fields = ["title", "description", "release_date"]
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }


class ImageGalleryForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ["image", "description"]


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["video_url", "description"]
