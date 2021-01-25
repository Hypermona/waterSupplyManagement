from django.db import models
from .Employee import Employee
from .Ward import Ward


class Meter(models.Model):
    meter_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    HEALTH = (
        ('G', 'GOOD'),
        ('O', 'OK'),
        ('B', 'BAD'),
    )
    meter_health = models.CharField(max_length=10, choices=HEALTH, null=True)

    class Meta:
        db_table = 'METER'

    @staticmethod
    def get_meter_by_username(username):
        try:
            return Meter.objects.get(employee=username)
        except:
            return False

    @staticmethod
    def get_meter_by_id(id_):
        return Meter.objects.filter(meter_id=id_)

    def register(self):
        self.save()
