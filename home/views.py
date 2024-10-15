from django.shortcuts import render, redirect, get_object_or_404
from home.models import Student, RemovedStudent

def student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        Email_id = request.POST.get('Email_id')
        age = request.POST.get('age')
        Date_of_birth = request.POST.get('Date_of_birth')
        Address = request.POST.get('Address')
        Course = request.POST.get('Course')
        Year_of_passing = request.POST.get('Year_of_passing')
        gender = request.POST.get('gender')
        passphoto = request.FILES.get('passphoto')
        Percentage=request.POST.get('percentage')
        # print(gender)
        try:
            Year_of_passing = int(Year_of_passing)
        except ValueError:
            return render(request, 'main.html', {'error': 'Invalid year format'})
        # print(Date_of_birth)
        student = Student.objects.create(
            name=name,
            mobile_no=mobile_no,
            Email_id=Email_id,
            age=age,
            Date_of_birth=Date_of_birth,
            Address=Address,
            Course=Course,
            Year_of_passing=Year_of_passing,
            gender=gender,
            passphoto=passphoto,
            Percentage=Percentage
        )

        return redirect('detail', pk=student.pk)

    return render(request, 'main.html')

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student
    }
    return render(request, 'individual.html', context)

def details(request):
    data = Student.objects.all()
    context = {
        'data': data
    }
    return render(request, 'details.html', context)


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.mobile_no = request.POST.get('mobile_no')
        student.Email_id = request.POST.get('Email_id')
        student.age = request.POST.get('age')
        # student.Date_of_birth = request.POST.get('Date_of_birth')
        student.Address = request.POST.get('Address')
        student.Course = request.POST.get('Course')
        student.Year_of_passing = request.POST.get('Year_of_passing')

        gender = request.POST.get('gender')
        # print(gender)
        if gender is None:
            print('1')
            student.gender=student.gender
        else:
            print('2')
            student.gender=gender

        
        student.Percentage = request.POST.get('percentage')

        passphoto = request.FILES.get('passphoto')
        if passphoto:
            student.passphoto = passphoto

        try:
            student.Year_of_passing = int(student.Year_of_passing)
        except ValueError:
            return render(request, 'edit_student.html', {'error': 'Invalid year format', 'student': student})
        student.save()
        return redirect('detail', pk=student.pk)

    return render(request, 'edit_student.html', {'student': student})

def search(request):
    query = request.GET.get('query', '')
    if query:
        results = Student.objects.filter(name__icontains=query)
    else:
        results = Student.objects.none()

    context = {
        'results': results,
        'query': query
    }
    return render(request, 'search.html', context)

def remove_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    print(student.Date_of_birth)
    RemovedStudent.objects.create(
        name=student.name,
        mobile_no=student.mobile_no,
        Email_id=student.Email_id,
        age=student.age,
        Date_of_birth=student.Date_of_birth,
        Address=student.Address,
        Course=student.Course,
        Year_of_passing=student.Year_of_passing,
        gender=student.gender,
        passphoto=student.passphoto,
        Percentage=student.Percentage
        
    )
    student.delete()
    return redirect('history')

def history(request):
    removed_students = RemovedStudent.objects.all()
    context = {
        'history': removed_students
    }
    return render(request, 'history.html', context)

def delete_student(request, pk):
    student = get_object_or_404(RemovedStudent, pk=pk)
    student.delete()
    return redirect('history')
