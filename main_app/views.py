from django.shortcuts import render, redirect
from .models import Student, Teacher, Course, Class, Grade
from .forms import StudentForm, TeacherForm, CourseForm, ClassForm, GradeForm


def index(request):
    return render(request, 'main_app/index.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'main_app/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'main_app/student_form.html', {'form': form})


def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'main_app/student_form.html', {'form': form})


def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'main_app/student_confirm_delete.html', {'student': student})
