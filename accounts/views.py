from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from guardian.shortcuts import assign_perm
from userena import settings
from userena import views as userena_views


# Create your views here.
# to be used to modify the userena profile page with my own template and views context
def dashboard(request):
    return render(request, "afrikalmarket/dashboard.html")
