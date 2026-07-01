from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# READ - List all students
def student_list(request):
    students = Student.objects.all().order_by('-enrollment_date')  # newest first
    return render(request, 'students/list.html', {'students': students})

# CREATE - Add a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:list')  # redirect to the list page
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form})

# READ - View a single student's details
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'student': student})

# UPDATE - Edit an existing student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/form.html', {'form': form})

# DELETE - Remove a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:list')
    return render(request, 'students/confirm_delete.html', {'student': student})