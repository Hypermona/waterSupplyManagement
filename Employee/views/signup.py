from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.Consumer import Consumer
from Employee.models.WaterBill import WaterBill
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Signup(View):
    def get(self, request):
        user = request.GET.get('user', False)
        return render(request, 'signup.html', {'user': user})

    def post(self, request):
        print(request.POST)
        user = request.POST.get('user', False)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email_id = request.POST.get('email_id')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        value = {
            "firstname": firstname,
            "lastname": lastname,
            "email_id": email_id,
            "username": username,
        }

        # Validationa
        error_message = None
        login_user = None
        if len(firstname) < 4:
            error_message = "First Name must be 4 char or large!"
        elif password1 != password2:
            error_message = "Password is not matching!"
        else:
            if user == 'consumer':
                login_user = Consumer.get_consumer_by_username(username)
            if user == 'consumer':
                login_user = Employee.get_employee_by_username(username)
            if login_user:
                error_message = "Username is already exist!!"

        print(firstname, lastname, email_id)
        print(user)
        if not error_message:
            # hashing
            password = make_password(password1)
            if user == 'consumer':
                consumer = Consumer(first_name=firstname,
                                    last_name=lastname,
                                    id=username,
                                    email_id=email_id,
                                    password=password
                                    )
                consumer.register()
            elif user == 'employee':
                employee = Employee(first_name=firstname,
                                    last_name=lastname,
                                    id=username,
                                    email_id=email_id,
                                    password=password
                                    )
                employee.register()
            request.session['user'] = username
            bills = WaterBill.get_all_bills_by_is_paid(username)
            return render(request, 'index.html', {'user': user, 'bills': bills})
        else:
            return render(request, 'signup.html', {'errorMessage': error_message, 'user': user, "values": value})
