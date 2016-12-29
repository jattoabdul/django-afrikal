from django.conf.urls import include, url
from userena import views as userena_views
from accounts import views as accounts_views
from accounts.forms import SellerSignupFormExtra, BuyersSignupFormExtra
from afrikalmarket import views as afrikalmarket_views

urlpatterns = [
    url(r'^signup/$', userena_views.signup, {'signup_form': BuyersSignupFormExtra}, name='userena_signup'),
    url(r'^signup/sellers/$', userena_views.signup, {'signup_form': SellerSignupFormExtra}, name='userena_signup_sellers'),
    url(r'^', include('userena.urls')),
    url(r'^', accounts_views.dashboard, name='dashboard'),
    url(r'^dashboard', accounts_views.dashboard, name='dashboard'),
]
