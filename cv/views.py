from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Employment, Education, Volunteering
from .forms import EmploymentForm, EducationForm, VolunteeringForm

def display_cv(request):
    employment = Employment.objects.all()
    education = Education.objects.all()
    volunteering = Volunteering.objects.all()
    return render(request, 'cv/cv.html', {'employment': employment, 'education': education, 'volunteering': volunteering, 'cv_page': 'active'})

@login_required
def education_new(request):
    if request.method == "POST":
            form = EducationForm(request.POST)
            if form.is_valid:
                form.save()
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
            form.save()
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
            form.save()
            return redirect('cv:display_cv')
    else:
        form = VolunteeringForm()

    return render(request, 'cv/volunteering_edit.html', {'form': form})

@login_required
def volunteering_edit(request, pk):
    volunteering = get_object_or_404(Volunteering, pk=pk)
    if request.method == "POST":
        form = VolunteeringForm(request.POST, instance=volunteering)
        if form.is_valid:
            form.save()
            return redirect('cv:display_cv')
    else:
        form = VolunteeringForm(instance=volunteering)
    
    return render(request, 'cv/volunteering_edit.html', {'form': form})

@login_required
def volunteering_remove(request, pk):
    volunteering = get_object_or_404(Volunteering, pk=pk)
    volunteering.delete()
    return redirect('cv:display_cv')

@login_required
def employment_new(request):
    if request.method == "POST":
        form = EmploymentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('cv:display_cv')
    else:
        form = EmploymentForm()

    return render(request, 'cv/employment_edit.html', {'form': form})