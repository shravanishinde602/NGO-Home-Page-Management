from django import forms

from .models import Project, ProjectImage


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})


class ProjectForm(BootstrapModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "short_description",
            "description",
            "goals",
            "beneficiaries",
            "impact_summary",
            "status",
            "category",
            "start_date",
            "end_date",
            "location",
            "team_partners",
            "image",
            "people_helped",
            "volunteers_engaged",
            "funds_raised",
            "order",
            "status_active",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class ProjectImageForm(BootstrapModelForm):
    class Meta:
        model = ProjectImage
        fields = ["project", "image", "caption"]
