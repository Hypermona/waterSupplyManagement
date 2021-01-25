from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from django.views import View

class ShowBill(View):
    def get(self, request):
        consumer = request.GET.get('consumer')
        print(request.GET.get('notpaid'))
        yrn =request.GET.get('notpaid')
        if yrn:
            print('hello worlsdddd')
            bills = WaterBill.get_all_bills_by_consumer(consumer,is_paid=False)
        else:
            bills = WaterBill.get_all_bills_by_consumer_all(consumer)
        print(bills)
        return render(request,'all_bill.html',{'bills':bills,'is_paid':yrn})