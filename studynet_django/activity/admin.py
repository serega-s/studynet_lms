from django.contrib import admin

from activity.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ["course", "lesson", "status"]
    list_filter = ["status", "course"]


admin.site.register(Activity, ActivityAdmin)
