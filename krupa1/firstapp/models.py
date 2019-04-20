from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.stu_name

class Schedule(models.Model):
    stu_name = models.ForeignKey('Student',on_delete=models.PROTECT)
    days = models.DateField()
    hours = models.IntegerField()

    def __str__(self):
        return self.days

class Fees(models.Model):
    days = models.ForeignKey('Schedule',on_delete=models.PROTECT)
    credited_fees = models.IntegerField()
    due_date = models.DateField()

    def __str__(self):
        return self.due_date

