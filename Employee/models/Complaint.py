from django.db import models
from .Consumer import Consumer


class Complaint(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    complaint_data = models.TextField(max_length=150)
    is_resolved = models.BooleanField(default=False,null=True)

    class Meta:
        db_table = 'COMPLAINTS'

    @staticmethod
    def get_all_complaints():
        return Complaint.objects.all()

    def delete_by_id(id_):
        return Complaint.objects.filter(id=id_).delete()

    def register(self):
        self.save()

    @staticmethod
    def get_complaint_by_complaint_id(c_id):
        try:
            return Complaint.objects.get(id=c_id)
        except:
            return False

    def get_complaint_by_consumer(consumer):
        return Complaint.objects.filter(consumer=consumer)
