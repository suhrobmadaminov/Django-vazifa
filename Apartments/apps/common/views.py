from django.shortcuts import render

# Create your views here.
def common_view(request):
    context = {
        'student_name': 'Ali',
        'score':95,
        'subject_list':["Math", "Informatika", "English"],
    }
    return render(request, 'index.html', context)