from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = locals()
    return render(request, "afrikalmarket/index.html", context_dict)

