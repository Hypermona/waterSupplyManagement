from django.shortcuts import render, redirect, HttpResponseRedirect
from Employee.models.Consumer import Consumer
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from Employee.models.Complaint import Complaint
from Employee.models.Ward import Ward
from Employee.models.Meter import Meter
from django.views import View


class MeterUp(View):
    def get(self, request):
        employee = request.GET.get('employee')
        meter = Meter.get_meter_by_username(employee)
        print('In meter up', meter.meter_id)
        return render(request, 'meter.html', {'meter': meter})

    def post(self, request):

        meter_id = request.POST.get('meter_id')
        health = request.POST.get('meter_health')
        meter = Meter.get_meter_by_id(meter_id)
        meter.update(meter_health=health)


        return redirect('updatereturn')