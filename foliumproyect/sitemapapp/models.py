import datetime
from email.policy import default
from tokenize import group
from django.db import models
import datetime

class Group(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.first_name+" "+self.last_name
        