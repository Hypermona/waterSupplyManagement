from django.db import models
from .Town import Town


class Ward(models.Model):
    class Meta:
        app_label = 'Employee'
        db_table = 'WARD'

    ward_id = models.AutoField(primary_key=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=40)



    def __str__(self):
        return str(self.ward_id)

    def get_ward_by_ward_id(wardid):
        try:
            return Ward.objects.get(ward_id=wardid)
        except:
            return False
