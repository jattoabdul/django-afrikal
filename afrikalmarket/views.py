from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "afrikalmarket/index.html")


# @login_required()
# def dashboard(request):
#     return render(request, "afrikalmarket/dashboard.html")
