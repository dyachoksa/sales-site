from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.flatpages.forms import FlatpageForm as BaseFlatpageForm


class FlatpageAdminForm(BaseFlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())
