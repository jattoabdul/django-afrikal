from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# setting the choices for languages below

LANGUAGES = (
                ('EN', 'English'),
                ('YR', 'Yoruba'),
                ('HS', 'Hausa'),
                ('IG', 'Igbo'),
               )
PROFICIENCY_LEVEL = (
                       (1, 'Fluent'),
                       (2, 'Moderate'),
                       (3, 'Beginner'),
                      )

# setting the choices for degree_title below
DEGREE_TITLE = (
            ('BSC', 'BSc'),
            ('BTC', 'Btech'),
            ('HND', 'HND'),
           )

GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
    )

# Create your models here.
class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    gender = models.PositiveSmallIntegerField(_('gender'),
                                              choices=GENDER_CHOICES,
                                              blank=True,
                                              null=True)
    website = models.URLField(_('website'), blank=True)
    location = models.CharField(_('location'), max_length=255, blank=True)
    about_me = models.TextField(_('about me'), blank=True)
    languages = models.CharField()
    skills = models.CharField(Skill)
    education = models.ForeignKey(Education, related_name='education')
    portfolio = models.CharField(Portfolio)
    certification = models.ForeignKey(Certification, related_name='certificates')

    def __str__(self):
        return u'%s %s %s' % (self.certificate, self.certified_from, self.certification_year)


class Language(models.Model):
    languages = models.CharField(choices=LANGUAGES,
                                 blank=True,
                                 null=True)
    proficiency = models.CharField(choices=PROFICIENCY_LEVEL,
                                    blank=True,
                                    null=True)

    def __str__(self):
        return u'%s %s' % (self.language, self.proficiency)
# ##


class Skill(models.Model):
    skill_type = models.CharField() # programming language

    def __str__(self):
        return u'%s' % self.skill_type
# ##


class Education(models.Model):
    school_country = models.CharField()
    school_name = models.CharField()
    degree_title = models.CharField(choice=DEGREE_TITLE) # set degree title choices
    degree_name = models.CharField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return u'%s %s' % (self.school_name, self.degree_title + '. ' + self.degree_name)
# ##


class Portfolio(models.Model):
    job_desc = models.CharField()
    job_url = models.URLField()

    def __str__(self):
        return u'%s %s ' % (self.job_desc, self.job_url)
# ##


class Certification(models.Model):
    certificate = models.CharField()
    certified_from = models.CharField()
    certification_year = models.DateField()

    def __str__(self):
        return u'%s %s %s' % (self.certificate, self.certified_from, self.certification_year)
# ##
