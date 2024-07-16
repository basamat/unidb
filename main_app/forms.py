from django import forms
from .models import Student, Teacher, Course, Class, Grade


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
