from django.db import models
from django import forms

# Create your models here.

choise = (('M', 'Male'), ('F', 'Female'))
business = (('Small', 'Small'),('Learge','Learge'), ('No', 'NO'))
region=(('M.P.', 'M.P.'),('Maharastra','Maharastra'), ('Bihar','Bihar'))
status=(('Solved', 'Solved'),('Inprogress','Inprogress'))

class Plans(models.Model):
	plan_name=models.CharField(max_length=100)
	speed_limit=models.CharField(max_length=50)
	duration=models.DurationField()
	prise=models.CharField(max_length=10)

	def __str__(self):
		return self.plan_name
	@classmethod
	def clasname(self):
		return 'Plans'

class PlanForm(forms.ModelForm):
	class Meta:
		model=Plans
		fields='__all__'



class Custmor(models.Model):
	name=models.CharField(max_length=50)
	contact=models.CharField(max_length=50)
	email=models.EmailField()
	age=models.IntegerField()
	region=models.CharField(max_length=10, choices=region)
	gander=models.CharField(max_length=10, choices=choise)
	business=models.CharField(max_length=10, choices=business)
	plan= models.ForeignKey(Plans, on_delete=models.CASCADE,related_name='plan')

	def __str__(self):
		return ( self.name +str(self.id))
	def detail(self):
		return (self.name+' ' +self.id)

	@classmethod
	def clasname(self):
		return 'Custmor'
class CustmorForm(forms.ModelForm):
	class Meta:
		model=Custmor
		fields='__all__'
		

class Compalin(models.Model):
	custmor= models.ForeignKey(Custmor, on_delete=models.CASCADE,related_name='users')
	description=models.CharField(max_length=500)
	date=models.DateField()
	status=models.CharField(max_length=20,choices=status,default=status[1][0])
	@classmethod
	def clasname(self):
		return 'Compalin'

class ComplainForm(forms.ModelForm):
	date=forms.DateField(widget = forms.SelectDateWidget())
	class Meta:
		model=Compalin
		fields=['custmor','description','date']
	


class Employ(models.Model):
	name=models.CharField(max_length=50)
	region=models.CharField(max_length=50)
	email=models.EmailField()
	contact=models.CharField(max_length=10)

	def __str__(self):
		return name
	@classmethod
	def clasname(self):
		return 'Employ'

class EmployForm(forms.ModelForm):
	class Meta:
		model=Employ
		fields='__all__'
	@classmethod
	def clasname(self):
		return 'Compalin'