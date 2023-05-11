from django.shortcuts import render
from portfolio import models

# Create your views here.
def portfolio(request):
    projects = models.Project.objects.all()
    return render(request, "portfolio/portfolio.html", {"projects": projects})