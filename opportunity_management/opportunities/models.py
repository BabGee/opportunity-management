from django.db import models


STAGE_CHOICES = (
 	('D','Discovery'),
 	('P','Proposal shared'),
	('N','Negotiations')
 )

class Account(models.Model):
	name = models.CharField(max_length=100, unique=True)
	address = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Opportunity(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=500, default='')
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	ammount = models.IntegerField(blank=True, null=True)
	stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='D')
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.get_stage_display()