from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import *
from django.utils import timezone
from .forms import *
from selenium import webdriver

# models test
class LoanTest(TestCase):
    def setUp(self):
        self.user1=User.objects.create(username='Edgar',email='eu@gmail.com',password='1080')
        self.user1.save()

        self.address = Address.objects.create(town='Nairobi',estate='Lavington',street_and_hse_no='1080',duration_in='2',user=self.user1)
        self.address.save()
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit
        User.objects.all().delete()
        Address.objects.all().delete()
    def test_call_view_denies_anonymous(self):
        response = self.client.get('/stepone/', follow=True)
        self.assertRedirects(response, '/login/?next=/stepone/')
        response = self.client.post('/steptwo/', follow=True)
        self.assertRedirects(response, '/login/?next=/steptwo/')        
    def test_creation_of_address(self):
        '''
        Testing Address Model
        '''
        self.assertTrue(isinstance( self.address, Address))
        self.assertEqual( self.address.__str__(),  self.address.town)

    def test_call_view_returns_redirection(self):
        '''
        using unit tests to check status codes for different view functions
        '''
        response = self.client.get('/stepone/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/steptwo/')
        self.assertEqual(response.status_code, 302)

    def test_valid_form(self):
        data = {'town': self.address.town, 'estate': self.address.estate,'street_and_hse_no':self.address.estate,'duration_in':self.address.duration_in,'user':self.user1}
        form = AddressForm(data=data)
        self.assertTrue(form.is_valid())
    def test_invalid_form(self):
        data = {'town': self.address.town, '': self.address.estate,'':self.address.estate,'duration_in':self.address.duration_in,'user':self.user1}
        form = AddressForm(data=data)
        self.assertFalse(form.is_valid())

    def test_signup_fire(self):
        self.driver.get("http://localhost:8000/stepsix/")
        self.driver.find_element_by_id('loanType').send_keys("test type")
        self.driver.find_element_by_id('purpose').send_keys("test purpose")
        self.driver.find_element_by_id('amount').send_keys("test amount")
        self.driver.find_element_by_id('submit').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)        
