from django.shortcuts import render, redirect, HttpResponseRedirect
from Employee.models.Consumer import Consumer
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from Employee.models.Complaint import Complaint
from Employee.models.Ward import Ward
from django.views import View


class AddComplaint(View):
    def get(self, request):
        consumer = request.GET.get('consumer')
        return render(request, 'add_complaint.html', {'consumer': consumer})

    def post(self, request):
        consumer = request.POST.get('consumer')
        data = request.POST.get('data')
        print("addComplaint", consumer, data)
        consumer_ = Consumer.get_consumer_by_username(consumer)
        print(consumer_)
        complaint = Complaint(consumer=consumer_, complaint_data=data)
        complaint.register()
        return render(request,'update_return.html')
