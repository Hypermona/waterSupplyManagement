from django.db import models


class Town(models.Model):
    town_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=30)

    class Meta:
        db_table = 'TOWN'

    def __str__(self):
        return self.location
