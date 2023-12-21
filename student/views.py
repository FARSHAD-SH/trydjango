from django.shortcuts import render
from .models import Teacher, Student
from django.db import connection
from django.db.models import Q

# Create your views here.
def student_list_view(request):

    # obj = Student.objects.get(id=1)
    # context = {
    #     'object': obj
    # }
    posts = Student.objects.all()
    print(posts)
    print(type(posts))
    print(posts.query)
    print(connection.queries)


    return render(request, "student/list.html", {'posts': posts})

def student_list_view(request):
    # posts = Student.objects.filter(surname__startswith='danesh') | Student.objects.filter(surname__startswith='shamlu')
    posts = Student.objects.filter(~Q(surname__startswith='danesh') | Q (surname__startswith='shamlu') | Q (surname__startswith='fasihiani'))

    print(posts)
    print(connection.queries)

    return render(request, "student/list.html", {'posts': posts})