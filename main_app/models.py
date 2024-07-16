from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    enrollment_date = models.DateField()
    faculty = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.CharField(max_length=50)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    grade_date = models.DateField()
