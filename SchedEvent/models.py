from django.db import models

# Create your models here.


#Student
class Student(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.id
#end of Student

#Teacher
class Teacher(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.id
#End of Teacher

