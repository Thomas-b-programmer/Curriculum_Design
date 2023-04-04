from django.db import models

# Create your models here.


#建立一个学生表模型
class database_Student(models.Model):
    student_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=20)
    math_score = models.CharField(max_length=10)
    chinese_score = models.CharField(max_length=10)
    english_score = models.CharField(max_length=10)
    total_score = models.CharField(max_length=10)