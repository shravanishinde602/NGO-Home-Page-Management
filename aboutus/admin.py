from django.contrib import admin

from .models import CoreValue, ImpactStatistic, OurStory, Program, TeamMember


@admin.register(OurStory)
class OurStoryAdmin(admin.ModelAdmin):
    list_display = ("heading", "updated_at")
    search_fields = ("heading", "introduction", "content")


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ("value", "order", "status")
    list_editable = ("order", "status")
    search_fields = ("value", "description")


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "status")
    list_editable = ("order", "status")
    search_fields = ("name", "description")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order", "status")
    list_editable = ("order", "status")
    search_fields = ("name", "role")


@admin.register(ImpactStatistic)
class ImpactStatisticAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "order", "status")
    list_editable = ("value", "order", "status")
    search_fields = ("label",)
