

from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_path']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PersonalParticularsForm(forms.ModelForm):
    class Meta:
        model = PersonalParticulars
        fields = ['membership_no', 'first_name', 'middle_name',
                  'last_name', 'id_no', 'dob', 'address', 'office_tel_no', 'mobile_no', 'pin_no', 'email', 'physical_address', 'marital_status', 'no_of_dependents'
                  ]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['town','estate','street_and_hse_no','duration_in','rent_owned']

class EmploymentDetailsForm(forms.ModelForm):
    class Meta:
        model = EmploymentDetails
        fields = ['applicants_employer','physical_address','postal_address','tel','designation','staff_no','employment_terms']

class BusinessTypeForm(forms.ModelForm):
    class Meta:
        model = BusinessType
        fields = ['bsn_type','business_income','rental_income','other_incomes','years_of_operations']

class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = ['account_name','account_no','bank','branch','bank_code','branch_code']


class LoanParticularsForm(forms.ModelForm):
    class Meta:
        model = LoanParticulars
        fields = ['loan_type','purpose_of_loan','amount']

class OtherLoansForm(forms.ModelForm):
    class Meta:
        model = OtherLoans
        fields = ['bank_name','amount_advanced','date_granted','reapyment_period','outstanding_balance','outstanding_balance']



