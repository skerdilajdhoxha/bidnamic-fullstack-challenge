from django.db import models


class BiddingSettingsChoices(models.TextChoices):
    HIGH = "HI", "High"
    MEDIUM = "ME", "Medium"
    LOW = "LO", "Low"


class Task(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(help_text="Should be entered, year-month-day")
    company_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=100, blank=True)
    bidding_settings = models.CharField(
        max_length=2, choices=BiddingSettingsChoices.choices, default=BiddingSettingsChoices.HIGH
    )
    google_ads_account_id = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
