from django.db import models


class address(models.Model):
    city = models.CharField(max_length = 50)


class student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)
    address = models.ForeignKey(address, on_delete=models.CASCADE)






