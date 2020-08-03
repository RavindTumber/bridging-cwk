from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Education, Volunteering
from .forms import EducationForm, VolunteeringForm

def display_cv(request):
    education = Education.objects.all()
    volunteering = Volunteering.objects.all()
    return render(request, 'cv/cv.html', {'education': education, 'volunteering': volunteering, 'cv_page': 'active'})

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

@login_required
def volunteering_new(request):
    if request.method == "POST":
        form = VolunteeringForm(request.POST)
        if form.is_valid:
            volunteering = form.save()
            return redirect('cv:display_cv')
    else:
        form = VolunteeringForm()

    return render(request, 'cv/volunteering_edit.html', {'form': form})