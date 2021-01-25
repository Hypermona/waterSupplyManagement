from django.shortcuts import render, redirect
from Employee.models.Employee import Employee
from Employee.models.Consumer import Consumer
from Employee.models.WaterBill import WaterBill
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self, request):
        user = request.GET.get('user', False)
        return render(request, 'login.html', {'user': user})

    def post(self, request):
        login_user = None
        bills = None
        user = request.POST.get('user', False)
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(F"User{user}")
        print(F"User{username}")
        print(F"User{password}")
        if user == 'consumer':
            login_user = Consumer.get_consumer_by_username(username)
            bills = WaterBill.get_all_bills_by_is_paid(username)
            print(F'bills by id {bills}')
        elif user == 'employee':
            login_user = Employee.get_employee_by_username(username)
        elif user == 'corporator':
            corp_user = authenticate(request, username=username, password=password)
            if corp_user is not None:
                login(request, corp_user)
                request.session['user'] = username
                return redirect("displaycorp")
            else:
                error_message = "Username/Password is incorrect!!"
                return render(request, 'login.html', {'errorMessage': error_message, 'user': user})
        print('login user', login_user)
        if login_user:
            if check_password(password, login_user.password):
                print(F"login user {login_user.id}")
                request.session['user'] = login_user.id
                return render(request, 'index.html', {'user': user, 'bills': bills})
            else:
                error_message = "Username/Password is incorrect!!"
                return render(request, 'login.html', {'errorMessage': error_message, 'user': user})
        else:
            error_message = "Username/Password is incorrect!!"
            return render(request, 'login.html', {'errorMessage': error_message, 'user': user})


def logout(request):
    request.session.clear()
    return redirect('homepage')
