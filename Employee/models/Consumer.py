from django.db import models
from .Ward import Ward


class Consumer(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField()
    password = models.CharField(max_length=200, )
    dob = models.DateField(null=True)
    # age = models.IntegerField()
    address = models.TextField(max_length=250, null=True)
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('N', 'NOTAPPLICABEL'),
    )
    gender = models.CharField(max_length=10, choices=GENDER, null=True)

    class Meta:
        db_table = 'CONSUMER'

    def __str__(self):
        return self.id

    @staticmethod
    def get_all_consumers():
        return Consumer.objects.all()

    @staticmethod
    def get_consumer_by_username(username):
        print(username)
        try:
            return Consumer.objects.get(id=username)
        except:
            return False

    def register(self):
        self.save()

    def delete_by_id(id):
        return Consumer.objects.filter(id=id).delete()
