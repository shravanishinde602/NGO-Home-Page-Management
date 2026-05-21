from django import forms

from .models import CoreValue, ImpactStatistic, OurStory, Program, TeamMember


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})


class OurStoryForm(BootstrapModelForm):
    class Meta:
        model = OurStory
        fields = [
            "heading",
            "introduction",
            "content",
            "banner_image",
            "mission_title",
            "mission_description",
            "vision_title",
            "vision_description",
        ]


class CoreValueForm(BootstrapModelForm):
    class Meta:
        model = CoreValue
        fields = ["value", "description", "order", "status"]


class ProgramForm(BootstrapModelForm):
    class Meta:
        model = Program
        fields = ["name", "description", "image", "order", "status"]


class TeamMemberForm(BootstrapModelForm):
    class Meta:
        model = TeamMember
        fields = ["name", "role", "image", "order", "status"]


class ImpactStatisticForm(BootstrapModelForm):
    class Meta:
        model = ImpactStatistic
        fields = ["label", "value", "order", "status"]
