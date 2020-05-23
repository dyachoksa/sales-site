from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as BaseFlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from .forms import FlatpageAdminForm
from .models import Employee


class FlatPageAdmin(BaseFlatPageAdmin):
    form = FlatpageAdminForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position")
    list_display_links = ("id", "name")
    # list_editable = ("position",)

    search_fields = ("name", "position")


admin.site.register(Employee, EmployeeAdmin)
