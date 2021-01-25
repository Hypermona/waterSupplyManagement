from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from Employee.models.Consumer import Consumer
from Employee.models.Complaint import Complaint
from django.views import View


class DisplayCorporator(View):
    def get(self, request):
        bills = WaterBill.get_all_bills()
        employees = Employee.get_all_employees()
        consumers = Consumer.get_all_consumers()
        complaints = Complaint.get_all_complaints()
        values = {'bills': bills,
                  'employees': employees,
                  'consumers': consumers,
                  'complaints': complaints
                  }
        return render(request, 'display_corporaor.html', values)

    def post(self, request):
        print(request)
        value = request.POST.get('value')
        delete_id = request.POST.get('id')
        print(value, delete_id)
        if value == 'WaterBill':
            WaterBill.delete_by_id(delete_id)
        if value == 'Employee':
            Employee.delete_by_id(delete_id)
        if value == 'Consumer':
            Consumer.delete_by_id(delete_id)
        if value == 'Complaint':
            Complaint.delete_by_id(delete_id)
        bills = WaterBill.get_all_bills()
        employees = Employee.get_all_employees()
        consumers = Consumer.get_all_consumers()
        complaints = Complaint.get_all_complaints()
        values = {'bills': bills,
                  'employees': employees,
                  'consumers': consumers,
                  'complaints': complaints
                  }
        return render(request, 'display_corporaor.html', values)
