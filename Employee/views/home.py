from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from Employee.models.Consumer import Consumer
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


# Create your views here.
def index(request):
    emp = Employee.get_all_employees()
    user = request.session.get("user")
    print(F'you are {request.session.get("user")}')
    return render(request, 'login.html', {'employees': emp})
