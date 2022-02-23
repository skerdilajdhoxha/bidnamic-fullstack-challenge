from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.test.client import Client
from .models import Task, BiddingSettingsChoices
from .forms import TaskCreateForm


class TaskTest(TestCase):
    def setUp(self):
        twenty_yrs_ago = timezone.now().date() - relativedelta(years=20)
        self.client = Client()
        self.test_user = User.objects.create_user('Jane', 'blah@blah.com', 'Doe')
        login = self.client.login(username='Jane', password='Doe')
        self.task = Task.objects.create(
            title="Test Title",
            first_name="John",
            surname="Smith",
            date_of_birth=twenty_yrs_ago,
            company_name="Bidnamic",
            address="",
            telephone="",
            bidding_settings=BiddingSettingsChoices.LOW,
            google_ads_account_id="dl9gjdll9a",
        )
        self.data = model_to_dict(self.task)

    def test_list_task_view(self):
        test_response = self.client.get('/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, "base.html")
        self.assertTemplateUsed(test_response, "tasks/task_list.html")

    def test_create_task_view(self):
        test_response = self.client.get("/create/")
        self.assertEqual(test_response.status_code, 200)
        test_response = self.client.post("/create/", {'data': self.data})
        self.assertEqual(Task.objects.count(), 1)
        self.assertTemplateUsed(test_response, "base.html")
        self.assertTemplateUsed(test_response, "tasks/create_task.html")

    def test_delete_task_view(self):
        test_response = self.client.post(f"/{self.task.pk}/delete/")
        self.assertEqual(test_response.status_code, 302)
        self.assertRedirects(test_response, reverse("task_list"), status_code=302)

    def test_clean_date_of_birth_is_less_than_eighteen(self):
        """
        We modify only the date_of_birth field with a wrong value
        """
        self.data['date_of_birth'] = timezone.now().date()
        form = TaskCreateForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_clean_google_ads_account_id_is_not_ten_letters(self):
        """
        We modify only the google_ads_account_id field with a wrong value
        """
        self.data['google_ads_account_id'] = 'different_from_10_letters'
        form = TaskCreateForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_date_of_birth_and_clean_google_ads_account_id(self):
        """
        Test both fields since the object is valid
        """
        form = TaskCreateForm(data=self.data)
        self.assertTrue(form.is_valid())
