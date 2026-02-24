from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    
    def __str__(self):
        return f"{self.emp_name} - {self.designation}"

    