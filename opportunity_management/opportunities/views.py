from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from opportunities.models import Opportunity
from opportunities.forms import AccountForm, OpportunityForm

from django.contrib import messages

@login_required
def index(request):
    context = {
        'all_opportunities' : Opportunity.objects.all()
    }
    return render(request, 'opportunities/index.html', context)

def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            form_name = form.cleaned_data.get('name')
            messages.success(request, f'Account {form_name} Created Successfully. You can now create opportunity for {form_name}')
            return redirect('create_opportunity')
    else:
        form = AccountForm()

    context = {
        'form': form,
        'form_name': 'Create Account' 
    }
    return render(request, 'opportunities/forms.html', context)

def create_opportunity(request):
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            form.save()
            form_name = form.cleaned_data.get('name')
            account_name = form.cleaned_data.get('account')
            messages.success(request, f'{form_name} successfully created for account {account_name}')
            return redirect('index')
    else:
        form = OpportunityForm()

    context = {
        'form' : form,
        'form_name' : 'Create Opportunity'
    }
    return render(request, 'opportunities/forms.html', context)                            