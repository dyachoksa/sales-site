from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from ..models import Employee


register = template.Library()

OUR_TEAM_TEMPLATE = "pages/_our_team.html"


@register.filter()
def with_our_team(text: str):
    output = text

    our_team_marker = "#our_team#"
    if our_team_marker in text:
        output = text.replace(our_team_marker, render_to_string(OUR_TEAM_TEMPLATE, our_team()))

    return mark_safe(output)


@register.inclusion_tag(OUR_TEAM_TEMPLATE)
def our_team(limit=5):
    staff = Employee.objects.all()[:limit]

    return {
        "content": "Our Team",
        "employee_list": staff,
    }
