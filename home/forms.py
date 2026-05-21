from django import forms

from .models import Banner, Initiative, NewsEvent, Partner, Statistic, Testimonial, VisionMission


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})


class BannerForm(BootstrapModelForm):
    class Meta:
        model = Banner
        fields = ["title", "description", "image", "order", "status"]


class VisionMissionForm(BootstrapModelForm):
    class Meta:
        model = VisionMission
        fields = ["vision_title", "vision_description", "mission_title", "mission_description"]


class StatisticForm(BootstrapModelForm):
    class Meta:
        model = Statistic
        fields = ["label", "value", "order", "status"]


class InitiativeForm(BootstrapModelForm):
    class Meta:
        model = Initiative
        fields = ["title", "description", "image", "order", "status"]


class NewsEventForm(BootstrapModelForm):
    class Meta:
        model = NewsEvent
        fields = ["title", "content", "image", "status"]


class TestimonialForm(BootstrapModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "message", "image", "status"]


class PartnerForm(BootstrapModelForm):
    class Meta:
        model = Partner
        fields = ["name", "logo", "status"]
