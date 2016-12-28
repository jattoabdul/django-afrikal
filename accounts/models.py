from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
import datetime

# setting the choices for languages below

# languages = (
#               'en',
#               'yr',
#               'hs',
#               'ig',
#               )
# proficiencyLevel = (
#                       'fluent',
#                       'moderate',
#                       'beginner',
#                      )

# setting the choices for degree_title below
# degree = (
#           'bsc',
#           'btech',
#           )


# Create your models here.
class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True,
                                verbose_name=_('user'), related_name='my_profile')
    favourite_snack = models.CharField(_('favouritesnack'), max_length=5)
#   description = model.TextField()
#   languages = (from a language choice, many to many selection)
#   linked account = (get setup for such)
#   skills = ( from skills model, many to many field)
#   education = (from education model, fields include 1.country of college/university, college/university name
#             2. degree title and 3. degree, 4. start date and 5. end/grad date, optional)
#   portfolio = (from portfolio model, fields include 1. job description, 2. job url, optional)
#   certification = ( from certificate model, fields include 1.certificate or Award, 2. certified from e.g adobe
#             and 3. year)
#   role = (buyers or sellers) -> get the role in for function by using get_profile_model function
#   gigs = (from gig models in afrikalmarket.model, field include 1.service title 2.service description(about gig)
#             3.service category 4.service subcategory, service images(1 or 3),  5.order details[type, price,
#             deliverydays, revisions, custom order=false], 6.skills4service[], 7.ratings)
#   offers = (offers table from the offers model in afrikalmarket.model)
# ##


# class Language(models.Model):
#   language = model.CharField(choice=languages)
#   proficiency = model.charField(choice=proficiencyLevel)
# ##


# class Skill(models.Model):
#   language = model.CharField()
# ##


# class Education(models.Model):
#     school_country = model.CharField()
#     school_name = model.CharField()
#     degree_title = model.CharField(choice=degreeTitle) # set degree title choices
#     degree_name = model.CharField()
#     start_date = model.DateTimeField()
#     end_date = model.DateTimeField()
# ##


# class Portfolio(models.Model):
#    job_desc = model.CharField()
#    job_url = model.UrlField()
# ##


# class Certification(models.Model):
#     certificate = model.CharField()
#     certified_from = model.CharField()
#     certification_year = model.DateField()
# ##


# creating the user's gig table(if he is a seller) when he signs up
# @receiver(post_save, sender=User)
# def create_user_gig_table(sender, instance, created, **kwargs):
#     if user.role is seller
#     MyGigs.objects.create(user=instance)
# ##


# creating  the user's offers table (both seller and buyer) when they sign up
# @receiver(post_save, sender=User)
# def create_user_offer_table(sender, instance, **kwargs):
#     MyOffers.object.create(user=instance)
# ##