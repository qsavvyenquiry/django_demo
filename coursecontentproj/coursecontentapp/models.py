from django.db import models

# Create your models here.


class Course(models.Model):

    course = models.CharField(max_length=150)
    content = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.course