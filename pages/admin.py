from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as BaseFlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from imagekit.admin import AdminThumbnail

from .forms import FlatpageAdminForm
from .models import Employee


class FlatPageAdmin(BaseFlatPageAdmin):
    form = FlatpageAdminForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position", "admin_thumbnail")
    list_display_links = ("id", "name")
    # list_editable = ("position",)

    search_fields = ("name", "position")

    readonly_fields = ("admin_thumbnail",)

    admin_thumbnail = AdminThumbnail(image_field="photo_80x80")


admin.site.register(Employee, EmployeeAdmin)
