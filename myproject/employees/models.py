from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
            return f'{self.id} - {self.name}'
class employee(models.Model):
    name = models.CharField(max_length=255)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    bonus = models.FloatField()
    def __str__(self):
            return f'{self.name} - {self.job_title} - {self.salary} - {self.department_id} - {self.bonus}'