from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from Employee.models.Ward import Ward
from Employee.models.Consumer import Consumer
from django.views import View


class Billgen(View):

    def get(self, request):
        employee = request.GET.get('employee')
        values = Employee.get_employee_by_username(employee)
        return render(request, 'bill_generator.html', {'employee': values})

    def post(self, request):
        ward = request.POST.get('ward')
        consumer = request.POST.get('consumer')
        collector = request.POST.get('collector')
        amount = request.POST.get('amount')
        read_value = request.POST.get('read_value')
        read_date = request.POST.get('read_date')
        due_date = request.POST.get('due_date')
        disconnection_date = request.POST.get('disconnection_date')
        ward_ = Ward.get_ward_by_ward_id(ward)
        consumer_ = Consumer.get_consumer_by_username(consumer)
        employee_ = Employee.get_employee_by_username(collector)
        bill = WaterBill(ward=ward_,
                         consumer=consumer_,
                         collector=employee_,
                         amount=amount,
                         read_date=read_date,
                         read_value=read_value,
                         is_paid=False,
                         due_date=due_date,
                         disconnection_date=disconnection_date,
                         )
        bill.register()
        return render(request, 'index.html', {'user': 'employee'})
