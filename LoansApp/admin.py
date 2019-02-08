from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)

admin.site.register(Address)
admin.site.register(PersonalParticulars)
admin.site.register(EmploymentDetails)
admin.site.register(BusinessType)
admin.site.register(BankDetails)
admin.site.register(LoanParticulars)
admin.site.register(OtherLoans)