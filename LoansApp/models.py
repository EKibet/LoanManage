from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
 
    profile_path = models.ImageField(
        upload_to='profile_pics/', default='profile_pics/default.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @classmethod
    def search_by_username(cls, search_term):
        search_result = cls.objects.filter(
            user__username__icontains=search_term)
        return search_result

    def save_profile(self):
        self.save()

class Address(models.Model):
    town = models.CharField(max_length=64)
    estate = models.CharField(max_length=64)
    street_and_hse_no = models.CharField(max_length=64)
    duration_in = models.CharField(max_length=64)
    rent_owned = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.town}'


class PersonalParticulars(models.Model):
    loan_no = models.IntegerField(null=False, default=0)
    membership_no = models.IntegerField(null=False, default=0)
    first_name = models.CharField(
        max_length=50, null=False)
    middle_name = models.CharField(max_length=50, default='User', null=False)
    last_name = models.CharField(max_length=50, default='User', null=False)
    id_no = models.IntegerField(null=False)
    dob = models.DateField(max_length=8)
    address = models.CharField(
        max_length=100, null=False)
    office_tel_no = models.IntegerField() 
    mobile_no = models.IntegerField()
    pin_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    physical_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=100)
    no_of_dependents = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.first_name}'


class EmploymentDetails(models.Model):
    loan_no = models.IntegerField(null=False, default=0)

    applicants_employer = models.CharField(max_length=64)
    physical_address = models.CharField(max_length=160)
    postal_address = models.CharField(max_length=160)
    tel = models.IntegerField()
    designation = models.CharField(max_length=100)
    staff_no = models.CharField(max_length=150)
    employment_terms = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.applicants_employer}'


class BusinessType(models.Model):
    loan_no = models.IntegerField(null=False, default=0)
    bsn_type = models.CharField(max_length=255)
    business_income = models.IntegerField()
    rental_income = models.IntegerField()
    other_incomes = models.IntegerField()
    years_of_operations = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.bsn_type}'


class BankDetails(models.Model):
    loan_no = models.IntegerField(null=False, default=0)
    account_name = models.CharField(max_length=255)
    account_no = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    bank_code = models.IntegerField()
    branch_code = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.account_name}'


class LoanParticulars(models.Model):
    loan_no = models.IntegerField(null=False, default=0)
    loan_type = models.CharField(max_length=255)
    purpose_of_loan = models.CharField(max_length=255)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.loan_type}'


class OtherLoans(models.Model):
    loan_no = models.IntegerField(null=False, default=0)
    bank_name = models.CharField(max_length=255)
    amount_advanced = models.IntegerField()
    date_granted = models.DateField()
    reapyment_period = models.IntegerField()
    outstanding_balance = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.bank_name}'


    
