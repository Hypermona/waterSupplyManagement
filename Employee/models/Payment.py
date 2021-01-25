from django.db import models
from .WaterBill import WaterBill
from .Consumer import Consumer
import datetime


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField(default=datetime.datetime.now)
    bill = models.ForeignKey(WaterBill, on_delete=models.CASCADE)
    METHOD = (
        ('ON', 'ONLINE'),
        ('OFF', 'OFFLINE'),
    )
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=10, choices=METHOD, null=True, default='Online')

    class Meta:
        db_table = 'PAYMENT'

    def register(self):
        self.save()
