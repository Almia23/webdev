from django.shortcuts import render
from .forms import StudentForm

def student_view(request):
    form = StudentForm()
    data = ''
    percent = None
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            total = cd['english'] + cd['physics'] + cd['chemistry']
            percent = total / 3
            data = f"{cd['name']}, {cd['dob']}, {cd['address']}, {cd['contact']}, {cd['email']}, Marks: {cd['english']}, {cd['physics']}, {cd['chemistry']}"
    return render(request, 'student.html', {'form': form, 'data': data, 'percent': percent})