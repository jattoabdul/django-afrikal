from django import forms
from userena.forms import SignupForm
from django.contrib.auth.models import Group

# references to Group created in admin
sellers = Group.objects.get(name='sellers')
buyers = Group.objects.get(name='buyers')


# different forms to add users to different role
class SellerSignupFormExtra(SignupForm):
    def save(self):
        new_user = super(SellerSignupFormExtra, self).save()
        new_user.groups.add(sellers)
        return new_user


class BuyersSignupFormExtra(SignupForm):
    def save(self):
        new_user = super(BuyersSignupFormExtra, self).save()
        new_user.groups.add(buyers)
        return new_user
