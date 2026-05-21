from django.db import models


class OrderedActiveModel(models.Model):
    order = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["order", "-id"]


class OurStory(models.Model):
    heading = models.CharField(max_length=140, default="About HopeBridge Foundation")
    introduction = models.TextField()
    content = models.TextField(help_text="Write the NGO background story or journey.")
    banner_image = models.ImageField(upload_to="about/story/", blank=True, null=True)
    mission_title = models.CharField(max_length=120, default="Our Mission")
    mission_description = models.TextField()
    vision_title = models.CharField(max_length=120, default="Our Vision")
    vision_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Our Story"
        verbose_name_plural = "Our Story"

    def __str__(self):
        return self.heading


class CoreValue(OrderedActiveModel):
    value = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value


class Program(OrderedActiveModel):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="about/programs/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TeamMember(OrderedActiveModel):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=120)
    image = models.ImageField(upload_to="about/team/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


class ImpactStatistic(OrderedActiveModel):
    label = models.CharField(max_length=90)
    value = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.label}: {self.value}"
