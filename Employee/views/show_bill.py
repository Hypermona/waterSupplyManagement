from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.WaterBill import WaterBill
from django.views import View


class ShowBill(View):

    def get(self, request):
        user = request.GET.get('consumer')
        print('showaaaaqqq', user)
        values = WaterBill.get_bill_by_username(user)
        print('showaaaa', values)
        return render(request, 'bill.html', {'bill': values})

    def post(self, request):
        ward = request.POST.get('ward')
        consumer = request.POST.get('consumer')
        collector = request.POST.get('collector')
        amount = request.POST.get('amount')
        read_date = request.POST.get('read_date')
        due_date = request.POST.get('due_date')
        disconnection_date = request.POST.get('disconnection_date')
        bill = WaterBill(ward=ward,
                         consumer=consumer,
                         collector=collector,
                         amount=amount,
                         read_date=read_date,
                         due_date=due_date,
                         disconnection_date=disconnection_date,
                         )
        bill.register()
        return redirect('homepage')
