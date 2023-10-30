from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class Plant(models.Model):
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Line(models.Model):
    name = models.CharField(max_length=50)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Machine(models.Model):
    machine_id = models.CharField(unique=True, max_length=5, validators=[MinLengthValidator(4)], default=None)
    tag_id = models.CharField(unique=True, max_length=8, default=None)
    name = models.CharField(max_length=50)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True)
    line = models.ForeignKey(Line, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Status(models.Model):
    working_choices = [('Yes', 'Yes'),
                       ('No', 'No')]
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True)
    line = models.ForeignKey(Line, on_delete=models.CASCADE, null=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    is_working = models.CharField(max_length=3, choices=working_choices)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    document_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        time = str(self.time)[:19]
        name = "{}-{}".format(self.machine, time)
        return name

    def get_absolute_url(self):
        return reverse('home')


class Scan(models.Model):
    time = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag[:20]

    def get_absolute_url(self):
        return reverse('history')
