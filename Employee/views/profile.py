from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.Consumer import Consumer
from Employee.models.WaterBill import WaterBill
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Profile(View):
    def get(self, request):
        users = request.GET.get('user')
        username = request.GET.get('username')
        print("profile", users, username)
        if users == "consumer":
            user = Consumer.get_consumer_by_username(username)
            return render(request, 'profile.html', {'user': user, "user_type": "consumer"})
        elif users == "employee":
            user = Employee.get_employee_by_username(username)
            return render(request, 'profile.html', {'user': user, "user_type": 'employee'})
        else:
            user = Employee.get_employee_by_username(username)
            return render(request, 'profile.html', {'user': user, "user_type": ''})

    # def post(self, request):
    #     bill_id = request.POST.get('bill_id')
    #     user = request.POST.get('user')
    #     bill = WaterBill.get_bill_by_bill_id(bill_id)
    #     bill.is_paid = True
    #     bill.register()
    #     bills = WaterBill.get_all_bills_by_is_paid(user)
    #     return render(request,'index.html',{'user':'consumer','bills':bills})
