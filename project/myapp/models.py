from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
import csv
from datetime import datetime


# Create your models here.
class customers(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.email


@receiver(pre_delete, sender=User)
def user_deleted_record(sender, instance, **kwargs):
    with open('deleted_user_records.csv', mode='a') as deleted_data:
        log_writer = csv.writer(deleted_data, delimiter=',')
        at_line_one = deleted_data.tell() == 0
        if at_line_one:
            log_writer.writerow(['Name', 'User ID', 'Deletion Time'])
        log_writer.writerow([instance.username, instance.id, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

