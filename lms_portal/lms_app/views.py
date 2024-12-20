from django.shortcuts import render
from .models import Reader

# Create your views here.



def home(request):
    return render(request,"home.html",context={"current_tab":"home"})

def readers(request):
    return render(request,"readers.html",context={"current_tab":"readers"})



def save_student(request):
    student_name = request.POST['student_name']
    return render(request,"welcome.html",context={'student_name': student_name})

from django.shortcuts import render
from .models import Reader

def readers_tab(request):
    readers = Reader.objects.all()
    return render(request, "readers.html", context={"current_tab": "readers", "readers": readers})



