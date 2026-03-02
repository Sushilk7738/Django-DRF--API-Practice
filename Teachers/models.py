from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    teacher_body = models.TextField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')
    subject = models.CharField()

    def __str__(self):
        return self.subject

