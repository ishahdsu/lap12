from django.db import models



class address(models.Model):
    city = models.CharField(max_length = 50)


class student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)
    address = models.ForeignKey(address, on_delete=models.CASCADE)


class card(models.Model):   
    card_number = models.CharField(max_length=20, unique=True)

class department(models.Model):
    name = models.CharField(max_length = 50)

class course(models.Model):
    title = models.CharField(max_length = 50)
    code =models.CharField(max_length=20, unique=True)

class studentlap9(models.Model):
    name = models.CharField(max_length = 50)
    card = models.OneToOneField(card, on_delete = models.PROTECT)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    course = models.ManyToManyField(course)


class address2(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city  

class student2(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    addresses = models.ManyToManyField(address2)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')












