from django.db import models

# create model here

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)   # optional
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name