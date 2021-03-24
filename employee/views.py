from django.shortcuts import render, redirect
from .models import Employees
from rest_framework import viewsets
from .serializers import EmployeesSerializer
from django.http import HttpResponse
import json


def home(request):
	msg = ''
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		designation = request.POST.get('designation')
		print(first_name)
		print(last_name)
		print(designation)
		try:
			if first_name and last_name and designation:
				user_details = Employees(first_name = first_name,
					last_name=last_name,designation=designation)
				user_details.save()
				msg = 'User Created!'
		except Exception as e:
			print(e)
			msg = 'User NOT added. Try Again.'

	return render(request, 'employee/home.html', {'msg':msg})


def show_employee(request):
	return render(request, 'employee/show_emp.html')

def get_data(request):
	if request.method == 'GET':
		designation = request.GET.get('designation')
		data = Employees.objects.filter(
			designation=designation)
		result = []
		for d in data:
			ser = EmployeesSerializer(d)
			result.append(ser.data)
		return HttpResponse(json.dumps(result))
	return render(request, 'employee/show_emp.html')