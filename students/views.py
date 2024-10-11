from django.shortcuts import render
from .models import Student

def board_view(request):
    students = Student.objects.prefetch_related('nominations').all()
    return render(request, 'students/board.html', {'students': students})
