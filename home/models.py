from django.db import models


class OrderedActiveModel(models.Model):
    order = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["order", "-id"]


class Banner(OrderedActiveModel):
    image = models.ImageField(upload_to="banners/", blank=True, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title


class VisionMission(models.Model):
    vision_title = models.CharField(max_length=120, default="Our Vision")
    vision_description = models.TextField()
    mission_title = models.CharField(max_length=120, default="Our Mission")
    mission_description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vision and Mission"
        verbose_name_plural = "Vision and Mission"

    def __str__(self):
        return "Vision and Mission"


class Statistic(OrderedActiveModel):
    label = models.CharField(max_length=80)
    value = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.label}: {self.value}"


class Initiative(OrderedActiveModel):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="initiatives/", blank=True, null=True)

    def __str__(self):
        return self.title


class NewsEvent(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="partners/", blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
