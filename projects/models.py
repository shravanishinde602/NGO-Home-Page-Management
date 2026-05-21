from django.db import models
from django.urls import reverse


class Project(models.Model):
    STATUS_CHOICES = [
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("upcoming", "Upcoming"),
    ]
    CATEGORY_CHOICES = [
        ("education", "Education"),
        ("health", "Health"),
        ("environment", "Environment"),
        ("community", "Community"),
    ]

    title = models.CharField(max_length=160)
    short_description = models.CharField(max_length=240, blank=True)
    description = models.TextField()
    goals = models.TextField(blank=True, help_text="Write main goals or objectives for this project.")
    beneficiaries = models.CharField(max_length=160, blank=True)
    impact_summary = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ongoing")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="community")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=160, blank=True)
    team_partners = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    people_helped = models.PositiveIntegerField(default=0)
    volunteers_engaged = models.PositiveIntegerField(default=0)
    funds_raised = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    status_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", args=[self.id])


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"Image for {self.project.title}"
