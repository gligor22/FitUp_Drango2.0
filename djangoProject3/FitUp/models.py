import datetime

import django.utils.timezone
from django.db import models
from enum import Enum
from django.contrib.auth.models import User


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    start_day = models.DateField(default=django.utils.timezone.now())
    gender = models.CharField(max_length=1)
    enters = models.IntegerField(default=0)
    allowed = models.IntegerField(default=0)
    remaining = models.IntegerField(default=0)

    def Enter(self):
        self.enters = self.enters+1

    def Cancel(self):
        if self.enters > 0:
            self.enters = self.enters-1

    def __str__(self):
        return self.first_name + " " + self.last_name


class Coach(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    start_day = models.DateField(default=django.utils.timezone.now())
    gender = models.CharField(max_length=1)
    rate = models.FloatField(default=0.0,)
    rate_num = models.IntegerField(default=0)
    num_week = models.IntegerField(default=0)
    num_month = models.IntegerField(default=0)
    num_year = models.IntegerField(default=0)
    num_all_trainings = models.IntegerField(default=0)

    def updateTrainings(self):
        self.num_week = self.num_week+1
        self.num_month = self.num_month + 1
        self.num_year = self.num_year + 1
        self.num_all_trainings = self.num_all_trainings+1

    def disagrate(self):
        if self.num_week > 0:
            self.num_week = self.num_week - 1
            self.num_month = self.num_month - 1
            self.num_year = self.num_year - 1
            self.num_all_trainings = self.num_all_trainings - 1

    def __str__(self):
        return self.first_name + " " + self.last_name


class Training(models.Model):
    class TrainingTypes(Enum):
        cardio = 'Cardio'
        plyo = 'Plyo'
        upper = 'Upper Body Workout'
        lower = 'Lower Body Workout'
        strenght = 'Strenght Training'
        metcon = 'Full Body Weight Training'

        @classmethod
        def choices(cls):
            print(tuple((i.name, i.value) for i in cls))
            return tuple((i.name, i.value) for i in cls)

    type = models.CharField(max_length=50, choices=TrainingTypes.choices())
    duration_min = models.IntegerField(default=60)
    datetime = models.DateTimeField()
    capacity = models.IntegerField(default=15)
    Coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        date = str(self.datetime).split('+')[0]
        return self.type.upper() + " - " + date


class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True)


class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=django.utils.timezone.now())
    num_trainings_per_week = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.client.first_name + " " + self.client.last_name + " / " + str(self.date) + " - " + str(self.price)

