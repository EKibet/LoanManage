from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!,You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html',{'form': form})

def landing_page(request):
    return render(request,'index.html')

@login_required
def create_loan_step1(request):
    address_form = AddressForm()
    # x= UserRegisterForm()
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        # personal_form = PersonalParticularsForm(request.POST)
        print('cool')
        if address_form.is_valid():
            print('valid')
            addressform = address_form.save(commit=False)
            addressform.user = request.user
            addressform.save()
            redirect('landing_page')
    else:
        address_form = AddressForm()

    return render(request, 'index.html', locals())    
@login_required
def create_loan_step2(request):
    personal_det_form = PersonalParticularsForm()
    user_address = Address.objects.get(user=request.user)
    # x= UserRegisterForm()
    if request.method == 'POST':
        personal_det_form = PersonalParticularsForm(request.POST)
        # personal_form = PersonalParticularsForm(request.POST)
        print(personal_det_form)
        if personal_det_form.is_valid():
            print('valid')
            form = personal_det_form.save(commit=False)
            form.user = request.user
            form.loan_no =123
            form.physical_address = user_address
            form.save()
            redirect('landing_page')
    else:
        personal_det_form = PersonalParticularsForm()

    return render(request, 'index.html', locals())    
@login_required
def create_loan_step3(request):
    employment_det_form = EmploymentDetailsForm()
    user_address = Address.objects.get(user=request.user)
    # x= UserRegisterForm()
    if request.method == 'POST':
        employment_det_form = EmploymentDetailsForm(request.POST)
        # personal_form = PersonalParticularsForm(request.POST)
        print('cool')
        if employment_det_form.is_valid():
            print('valid')
            form = employment_det_form.save(commit=False)
            form.user = request.user
            form.loan_no =123
            form.save()
            redirect('landing_page')
    else:
        employment_det_form = EmploymentDetailsForm()

    return render(request, 'index.html', locals())    

def create_loan_step4(request):
    bsn_det_form = BusinessTypeForm()
    user_address = Address.objects.get(user=request.user)
    # x= UserRegisterForm()
    if request.method == 'POST':
        bsn_det_form = BusinessTypeForm(request.POST)
        # personal_form = PersonalParticularsForm(request.POST)
        print('cool')
        if bsn_det_form.is_valid():
            print('valid')
            form = bsn_det_form.save(commit=False)
            form.user = request.user
            form.loan_no =123
            form.save()
            redirect('landing_page')
    else:
        bsn_det_form = BusinessTypeForm()

    return render(request, 'index.html', locals())  
@login_required
def create_loan_step5(request):
    bank_det_form = BankDetailsForm()
    user_address = Address.objects.get(user=request.user)
    # x= UserRegisterForm()
    if request.method == 'POST':
        bank_det_form = BankDetailsForm(request.POST)
        print('cool')
        if bank_det_form.is_valid():
            print('valid')
            form = bank_det_form.save(commit=False)
            form.user = request.user
            form.loan_no =123
            form.save()
            redirect('landing_page')
    else:
        bank_det_form = BankDetailsForm()

    return render(request, 'index.html', locals()) 
@login_required
def create_loan_step6(request):
    loan_det_form = LoanParticularsForm()
    user_address = Address.objects.get(user=request.user)
    # x= UserRegisterForm()
    if request.method == 'POST':
        loan_det_form = LoanParticularsForm(request.POST)
        print('cool')
        if loan_det_form.is_valid():
            print('valid')
            form = loan_det_form.save(commit=False)
            form.user = request.user
            form.loan_no =123
            form.save()
            redirect('landing_page')
    else:
        loan_det_form = LoanParticularsForm()

    return render(request, 'index.html', locals())  
@login_required
def create_loan_step7(request):
    other_det_form = OtherLoansForm()
    user_address = Address.objects.get(user=request.user)
    # x= UserRegisterForm()
    if request.method == 'POST':
        other_det_form = OtherLoansForm(request.POST)
        print('cool')
        if other_det_form.is_valid():
            print('valid')
            form = other_det_form.save(commit=False)
            form.user = request.user
            form.loan_no =123
            form.save()
            redirect('')
    else:
        other_det_form = OtherLoansForm()

    return render(request, 'index.html', locals())  


@login_required
def delete_loan(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)
    if request.user != loan.owner:
        return redirect('/')

    if request.method == "POST":
        loan.delete()
        messages.success(
                        request,
                        'Loan Deleted Successfully',
                        extra_tags='alert alert-success alert-dismissible fade show'
                        )
        return redirect('loans:list')

    return render(request, 'index.html', locals())

@login_required
def edit_loan(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)
    if request.user != loan.owner:
        return redirect('/')

    if request.method == "POST":
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            messages.success(
                            request,
                            'Loan Edited Successfully',
                            extra_tags='alert alert-success alert-dismissible fade show'
                            )
            return redirect('loans:list')
    else:
        form = LoanForm(instance=loan)

    return render(request, 'index.html', locals())
