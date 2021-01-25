from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.Consumer import Consumer
from Employee.models.WaterBill import WaterBill
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from Employee.models.Payment import Payment


class Payment(View):
    def get(self, request):
        bill_id = request.GET.get('bill_id')

        bill = WaterBill.get_bill_by_bill_id(bill_id)
        print('inside payment bill=', bill.bill_id)
        return render(request, 'payment.html', {'bill': bill})

    def post(self, request):
        bill_id = request.POST.get('bill_id')
        user = request.POST.get('user')
        bill = WaterBill.get_bill_by_bill_id(bill_id)
        consumer = Consumer.get_consumer_by_username(user)
        bill.is_paid = True
        bill.register()
        bills = WaterBill.get_all_bills_by_is_paid(user)
        return render(request, 'index.html', {'user': 'consumer', 'bills': bills})
