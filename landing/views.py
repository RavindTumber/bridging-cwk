from django.shortcuts import render

def home_view(request):
    # add a context so that the respective page will have the active class applied within the base.html
    return render(request, 'landing/index.html', {'home_page': 'active'})