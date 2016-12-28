from django.conf.urls import include, url
from userena import views as userena_views
# from accounts.forms import SignupForm
from accounts import views

urlpatterns = [
    # url(r'^userena/signup/$', userena_views.signup, name='account_signup'), # {'template_name': 'signin.html'},
    # {'signup_form': SignupForm},
    url(r'^', include('userena.urls')),
    # url(r'^userena/profile/$', userena_views.profile_detail, name='account_profile'),
]
