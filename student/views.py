from django.shortcuts import render
from .models import Teacher, Student

# Create your views here.
def student_list_view(request):

    obj = Student.objects.get(id=1)
    context = {
        'object': obj
    }

    return render(request, "student/list.html", context)