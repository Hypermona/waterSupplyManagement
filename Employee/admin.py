from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.Employee import Employee
from .models.Consumer import Consumer
from .models.Complaint import Complaint
from .models.Ward import Ward
from .models.Town import Town
from .models.Meter import Meter
from .models.WaterBill import WaterBill
from .models.Payment import Payment


# Register your models here.
# class AdminEmployee(admin.UserAdmin):
#     list_display = ['employee_id', 'first_name', 'last_name', 'email_id', 'dob', 'salary', 'address', 'gender']


class AdminEmployee(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email_id', 'dob', 'salary', 'address', 'gender', ]


class AdminConsumer(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email_id', 'dob', 'address', 'gender', ]


class AdminComplaint(admin.ModelAdmin):
    list_display = ['consumer', 'complaint_data']


class AdminTow(admin.ModelAdmin):
    list_display = ['town_id', 'location']


class AdminWard(admin.ModelAdmin):
    list_display = ['ward_id', 'town', 'member_name']


class AdminWaterBill(admin.ModelAdmin):
    list_display = ['bill_id', 'ward', 'consumer','collector', 'amount', 'is_paid', 'read_date','due_date', 'disconnection_date',]


admin.site.register(Employee, AdminEmployee)
admin.site.register(Consumer, AdminConsumer)
admin.site.register(Complaint, AdminComplaint)
admin.site.register(Town, AdminTow)
admin.site.register(Ward, AdminWard)
admin.site.register(Meter)
admin.site.register(WaterBill, AdminWaterBill)