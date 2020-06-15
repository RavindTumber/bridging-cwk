from django.shortcuts import render

def display_cv(request):
    return render(request, 'cv/cv.html', {})