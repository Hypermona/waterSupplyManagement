from django.shortcuts import render, redirect, HttpResponseRedirect
from Employee.models.Consumer import Consumer
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from Employee.models.Complaint import Complaint
from Employee.models.Ward import Ward
from django.views import View

class UpdateReturn(View):
    def get(self,request):
        return render(request, 'update_return.html')