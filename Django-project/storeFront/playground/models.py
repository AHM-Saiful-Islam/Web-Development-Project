from django.db import models

# create model-class member contains 5 fields
class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    age = models.IntegerField()

    # object name in database; object means name of every instance in database
    def __str__(self) -> str:
        return self.fname + ' ' + self.lname

# create model-class Product contains 6 fields
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    stock = models.IntegerField()
    category = models.CharField(max_length=200)
    price = models.FloatField()
    company = models.CharField(max_length=500)

    # object name in database; object means name of every instance in database
    def __str__(self) -> str:
        return self.name + ' from ' + self.company