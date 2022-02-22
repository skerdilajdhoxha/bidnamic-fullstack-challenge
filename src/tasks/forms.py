from django import forms
from django.utils import timezone

from dateutil.relativedelta import relativedelta

from .models import Task
from .widgets import DateTimeInput


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {"date_of_birth": DateTimeInput()}

    def clean_date_of_birth(self):
        eighteen_yrs = timezone.now().date() - relativedelta(years=18)
        print(
            self.cleaned_data["date_of_birth"],
            "========",
            timezone.now().date(),
            "=============",
            eighteen_yrs,
            "-----------------",
            timezone.now().date() - self.cleaned_data["date_of_birth"],
        )

        date_of_birth = self.cleaned_data["date_of_birth"]
        if date_of_birth > timezone.now().date():
            raise forms.ValidationError("Date cannot be later than today.")
        return date_of_birth
