from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import assign_perm
from userena import settings
from userena import views as userena_views
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group


# Create your views here.
# logic for buyers dashboard view
@login_required()
@user_passes_test(lambda u: Group.objects.get(name='buyer') in u.groups.all())
def dashboard(request):
    # Logic for buyer dashboard
    context_dict = locals()
    return render(request, "afrikalmarket/dashboard.html", context_dict)


# logic for sellers dashboard view
@login_required()
@user_passes_test(lambda u: Group.objects.get(name='sellers') in u.groups.all())
def dashboard_seller(request):
    # Logic for seller dashboard
    context_dict = locals()
    return render(request, "afrikalmarket/dashboard_seller.html", context_dict)
