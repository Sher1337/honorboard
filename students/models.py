from django.db import models

class Nomination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    nominations = models.ManyToManyField(Nomination, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
