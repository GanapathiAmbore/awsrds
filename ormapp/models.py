from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    year=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    year=models.DateField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

