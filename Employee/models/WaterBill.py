from django.db import models
from .Consumer import Consumer
from .Employee import Employee
from .Ward import Ward


class WaterBill(models.Model):
    class Meta:
        app_label = 'Employee'
        db_table = 'WATERBILL'

    bill_id = models.AutoField(primary_key=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, )
    collector = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    read_value = models.IntegerField()
    read_date = models.DateField()
    due_date = models.DateField()
    disconnection_date = models.DateField()

    def get_bill_by_username(username):
        print(username)
        try:
            return WaterBill.objects.filter(consumer=username).order_by('read_date')[0]
        except:
            return False

    @staticmethod
    def get_all_bills():
        return WaterBill.objects.all()

    @staticmethod
    def get_bill_by_bill_id(billid):
        print("inside water bill billid is", billid)
        try:
            return WaterBill.objects.get(bill_id=billid)
        except:
            return False

    @staticmethod
    def get_all_bills_by_consumer(consumer, is_paid):
        print('inside fu', consumer)
        return WaterBill.objects.filter(consumer=consumer, is_paid=is_paid)

    @staticmethod
    def get_all_bills_by_consumer_all(consumer):
        print('inside fu', consumer)
        return WaterBill.objects.filter(consumer=consumer)

    @staticmethod
    def get_all_bills_by_is_paid(consumer):
        return WaterBill.objects.filter(consumer=consumer, is_paid=False)[0:2]

    def register(self):
        self.save()

    def delete_by_id(delete_id):
        print('inside delete', delete_id)
        return WaterBill.objects.filter(bill_id=delete_id).delete()
