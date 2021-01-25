from django.db import models
# from djtriggers.models import Trigger
from datetime import date


# Create your models here.
class Employee(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField()
    password = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    # age = models.IntegerField()
    salary = models.IntegerField(null=True)
    address = models.TextField(max_length=250, null=True)
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('N', 'NOTAPPLICABEL'),
    )
    gender = models.CharField(max_length=10, choices=GENDER, null=True)

    class Meta:
        db_table = 'EMPLOYEE'

    # def _process(self, dictionary={}):
    #     age = self.dob.year - date.today().year

    @staticmethod
    def get_all_employees():
        return Employee.objects.all()

    @staticmethod
    def get_employee_by_username(username):
        print(username)
        try:
            return Employee.objects.get(id=username)
        except:
            return False

    def register(self):
        self.save()

    def __str__(self):
        return self.id

    def delete_by_id(id):
        return Employee.objects.filter(id=id).delete()