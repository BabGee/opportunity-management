from django.forms import ModelForm

from .models import Account, Opportunity

class AccountForm(ModelForm):
	class Meta:
		model = Account
		fields = '__all__'


class OpportunityForm(ModelForm):
	class Meta:
		model = Opportunity
		fields = '__all__'
