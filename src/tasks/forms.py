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
        """Must be more than 18 to create a task."""
        eighteen_yrs_ago = timezone.now().date() - relativedelta(years=18)
        date_of_birth = self.cleaned_data["date_of_birth"]
        if date_of_birth > eighteen_yrs_ago:
            raise forms.ValidationError("You have to be +18 to create a task.")
        return date_of_birth

    def clean_google_ads_account_id(self):
        """Google Ads account ID should be 10 letters."""
        google_ads_account_id = self.cleaned_data["google_ads_account_id"]
        if len(google_ads_account_id) != 10:
            raise forms.ValidationError("Your Google account must be ten letters.")
        return google_ads_account_id
