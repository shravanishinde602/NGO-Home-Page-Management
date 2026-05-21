from django.contrib import admin

from .models import Banner, Initiative, NewsEvent, Partner, Statistic, Testimonial, VisionMission


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "status")
    list_editable = ("order", "status")
    search_fields = ("title",)


@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ("vision_title", "mission_title", "last_updated")


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "order", "status")
    list_editable = ("value", "order", "status")


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "status")
    list_editable = ("order", "status")
    search_fields = ("title",)


@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "status")
    list_filter = ("status", "created_at")
    search_fields = ("title", "content")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    list_editable = ("status",)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    list_editable = ("status",)
