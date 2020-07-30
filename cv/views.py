from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Education
from .forms import EducationForm

def display_cv(request):
    educations = Education.objects.all()
    return render(request, 'cv/cv.html', {'educations': educations, 'cv_page': 'active'})

@login_required
def education_new(request):
    if request.method == "POST":
            form = EducationForm(request.POST)
            if form.is_valid:
                education = form.save()
                return redirect('cv:display_cv')
    else:
        form = EducationForm()

    return render(request, 'cv/education_edit.html', {'form': form})

@login_required
def education_edit(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)
        if form.is_valid:
            education = form.save()
            return redirect('cv:display_cv')
    else:
        form = EducationForm(instance=education)
    
    return render(request, 'cv/education_edit.html', {'form': form})

@login_required
def education_remove(request, pk):
    education = get_object_or_404(Education, pk=pk)
    education.delete()
    return redirect('cv:display_cv')