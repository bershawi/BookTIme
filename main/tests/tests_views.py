from django.test import TestCase
from django.urls import reverse         #This lib for removing url from test case
from main import forms


class TestPage(TestCase):

    #Test case for Home.html
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')

    #Test case for  about-us.html
    def test_about_us_page_works(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertContains(response,"BookTime")

    #Test case for contact_form.html
    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'contact_form.html')
        self.assertContains(response,'BookTime')
        self.assertIsInstance(response.context["form"],forms.ContactForm)