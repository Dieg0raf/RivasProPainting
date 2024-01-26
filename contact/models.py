from django.db import models

class Projects(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=50)
    user_phone = models.CharField(max_length=12)
    job_desc = models.TextField(blank=True)

    JOB_CHOICES = [
        ('', 'What type of painting'),
        ('Interior', 'Interior'),
        ('Exterior', 'Exterior'),
    ]

    job = models.CharField(max_length=20, choices=JOB_CHOICES, default='', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"