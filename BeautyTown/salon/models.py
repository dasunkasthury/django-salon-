from django.db import models
from enum import Enum


class Salon(models.Model):
    salon_name = models.CharField(max_length=250)

    def __str__(self):
        return self.salon_name


class Job(models.Model):
    JobStatus = (
        ('FULL-TIME', 'full-time'),
        ('PART-TIME', 'part-time'),
    )
    job_title = models.CharField(max_length=250)
    date = models.DateField()
    type = models.CharField(max_length=250, choices=JobStatus, default='FULL-TIME')

    def __str__(self):
        return self.job_title


class Timeslot(models.Model):
    SessionStatus = (
        ('FREE', 'free'),
        ('BUSY', 'busy'),
    )

    day = models.DateField()
    evening = models.CharField(max_length=250, choices=SessionStatus, default='FREE')
    morning = models.CharField(max_length=250, choices=SessionStatus, default='FREE')

    def __str__(self):
        return self.evening


class Freelancer(models.Model):
    StatusType = (
        ('Stylist', 'Stylist'),
        ('Educator', 'Educator'),
    )

    freelancer_name = models.CharField(max_length=250)
    age = models.IntegerField()
    value = models.IntegerField()
    type = models.CharField(max_length=250, choices=StatusType, default='Stylist')
    time_slot_id = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.freelancer_name


class Book(models.Model):
    StatusChoices = (
        ('PENDING', 'pending'),
        ('CONFIRMED', 'confirmed'),
    )

    StatusPayment = (
        ('PENDING', 'pending'),
        ('PAYED', 'payed'),
    )

    RatingStatus = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    book_status = models.CharField(max_length=250, choices=StatusChoices, default='PENDING')
    payment = models.IntegerField()
    payment_status = models.CharField(max_length=250, choices=StatusPayment, default='PENDING')
    rating = models.CharField(max_length=250, choices=RatingStatus, default='5')
    salon_id = models.ForeignKey(Salon, on_delete=models.CASCADE)
    freelancer_id = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_status
