from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView
from .models import *
from .models import PlanForm
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin



from django.urls import reverse_lazy

class Index(LoginRequiredMixin,View):
	template_name='index.html'
	def get(self,request):
		k={x.clasname():x.objects.count() for x in (Plans,Custmor,Compalin,Employ)}
		print(k)
		return render(request,self.template_name,{'k':k})

		
class PlanDelete(LoginRequiredMixin,SuccessMessageMixin,View):
	def get(self,request,pk):
		name=Plans.objects.filter(id=pk).delete()
		return redirect('plans')


class PlanData(LoginRequiredMixin,ListView):
	model=Plans
	template_name='plans.html'
	context_object_name = 'object'

class Planadd(LoginRequiredMixin,View):
	template_name='addplan.html'
	def get(self,request):
		form=PlanForm()
		return render(request,self.template_name,{'form':form})
	def post(self,request):
		data=PlanForm(request.POST)
		if data.is_valid():
			data.save()
			messages.success(request, 'Form submission successful')
			return redirect ('planadd')
		else:
			messages.success(request, 'View the valid details')
			return redirect ('planadd')
			
class PlanUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
	model = Plans
	fields = ['plan_name','speed_limit','duration','prise']
	template_name='addplan.html'
	def get_success_url(self):
            return reverse('plans')

class EmployeeDelete(LoginRequiredMixin,View):
	def get(self,request,pk):
		name=Employ.objects.filter(id=pk).delete()
		return redirect('employee')

class EmployeeData(LoginRequiredMixin,ListView):
	model=Employ
	template_name='employee.html'
	context_object_name = 'object'

class Employeeadd(LoginRequiredMixin,View):
	template_name='addemployee.html'
	def get(self,request):
		form=EmployForm()
		return render(request,self.template_name,{'form':form})
	def post(self,request):
		data=EmployForm(request.POST)
		if data.is_valid():
			data.save()
			messages.success(request, 'Form submission successful')
			return redirect('employeeadd')
		else:
			return HttpResponse('not working')
class EmployeeUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
	model = Employ
	fields = '__all__'
	template_name='addemployee.html'
	def get_success_url(self):
            return reverse('employee')


'''
def get_context_data(self, **kwargs):
        context = super(BillListView, self).get_context_data(**kwargs)
        context['budgets'] = Budget.objects.filter(category__exact='bill') //filter as per required
        return context'''


class CustmorData(LoginRequiredMixin,View):
	template_name='custmor.html'
	form=CustmorForm()
	def get(self,request):
		return render(request,self.template_name,{'form':self.form})
	def post(self,request):
		data=CustmorForm(request.POST)
		if data.is_valid():
			data.save()
			messages.success(request, 'Form submission successful')
			return redirect('custmor')





class CustmorView(LoginRequiredMixin,ListView):
	model=Custmor
	template_name='custmordata.html'
	context_object_name = 'object'


class Complainadd(LoginRequiredMixin,View):
	template_name='addcomplain.html'
	form=ComplainForm()
	def get(self,request):
		return render(request,self.template_name,{'form':self.form})
	def post(self,request):
		data=ComplainForm(request.POST)
		if data.is_valid():
			data.save()
			messages.success(request, 'Complain has been submitted')
			return redirect('complain')


class ComplainView(LoginRequiredMixin,ListView):
	model=Compalin
	template_name='complainview.html'

	context_object_name = 'object'



class ComplainDelete(LoginRequiredMixin,SuccessMessageMixin,View):
	def get(self,request,pk):
		name=Compalin.objects.filter(id=pk).delete()
		return redirect('complainview')

class ComplainUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
	model = Compalin
	fields ='__all__'
	template_name='updatecomplain.html'
	def get_success_url(self):
            return reverse('complainview')


class ComplainUpdateStatus(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
	model = Compalin
	fields =['custmor','status']
	template_name='updatecomplain.html'
	def get_success_url(self):

            return reverse('complainview')
           