from django.shortcuts import render, redirect, HttpResponseRedirect
from Employee.models.Consumer import Consumer
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from Employee.models.Complaint import Complaint
from Employee.models.Ward import Ward
from django.views import View


class UpdateForm(View):
    def get(self, request):
        type_ = request.GET.get('type_')
        username = request.GET.get('username')
        next = request.POST.get('next', '/')
        print(type_)
        if type_ == 'consumer':
            consumer = Consumer.get_consumer_by_username(username)
            return render(request, 'consumer_form.html', {'consumer': consumer})
        elif type_ == 'employee':
            employee = Employee.get_employee_by_username(username)
            return render(request, 'employee_form.html', {'employee': employee})
        elif type_ == 'bill':
            bill = WaterBill.get_bill_by_bill_id(username)
            return render(request, 'bill_form.html', {'bill': bill})
        elif type_ == 'complaint':
            complaint = Complaint.get_complaint_by_complaint_id(username)
            return render(request, 'complaint_form.html', {'complaint': complaint})

    def post(self, request):
        print(request.POST)
        type_ = request.POST.get('type_')
        username = request.POST.get('username')
        next = request.POST.get('next', '/')
        print(next)
        print('update from consumer', type_, username)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if type_ == 'consumer':
            consumer = Consumer.get_consumer_by_username(username)
            consumer.first_name = first_name
            consumer.last_name = last_name
            consumer.email = email
            consumer.dob = dob
            consumer.gender = gender
            consumer.address = address
            consumer.register()
            consumer = Consumer.get_consumer_by_username(username)
            bills = WaterBill.get_all_bills_by_is_paid(consumer.id)
            return redirect('updatereturn')

        elif type_ == 'employee':
            employee = Employee.get_employee_by_username(username)
            employee.first_name = first_name
            employee.last_name = last_name
            employee.email = email
            employee.dob = dob
            employee.gender = gender
            employee.address = address
            employee.register()
            consumer = Employee.get_employee_by_username(username)
            bills = WaterBill.get_all_bills_by_is_paid(consumer.id)
            return redirect('updatereturn')

        elif type_ == "bill":
            ward = request.POST.get('ward')
            consumer = request.POST.get('consumer')
            collector = request.POST.get('collector')
            amount = request.POST.get('amount', 100)
            read_value = request.POST.get('read_value')
            read_date = request.POST.get('read_date')
            due_date = request.POST.get('due_date')
            disconnection_date = request.POST.get('disconnection_date')
            ward_ = Ward.get_ward_by_ward_id(ward)
            consumer_ = Consumer.get_consumer_by_username(consumer)
            employee_ = Employee.get_employee_by_username(collector)
            bill = WaterBill.get_bill_by_bill_id(id)
            bill.ward = ward_
            bill.consumer = consumer_
            bill.amount = amount
            bill.employee = employee_
            bill.read_value = read_value
            bill.read_date = read_date
            bill.due_date = due_date
            bill.disconnection_date = disconnection_date
            bill.register()
            return redirect('updatereturn')


        elif type_ == "complaint":
            consumer = request.POST.get('consumer')
            id_ = request.POST.get('id')
            data = request.POST.get('complaint_data')
            is_resolved = request.POST.get('is_resolved')
            complaint = Complaint.get_complaint_by_complaint_id(id_)
            complaint.complaint_data = data
            complaint.is_resolved = is_resolved

            complaint.register()
            return redirect('displaycorp')
