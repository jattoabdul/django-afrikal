from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from guardian.shortcuts import get_perms_for_model
from guardian.shortcuts import get_perms
from django.utils.translation import ugettext as _


MYGIGS_PERMISSIONS = (
            ('view_gig', 'Can view gig'),
)

PLANS = (
        ('BS', 'Basic'),
        ('PM', 'Premium'),
        ('CM', 'Custom'),
    )


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_frik_cat', None, {'slug': self.slug}
# ##


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    parent_category = models.ManyToOneRel(Category)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Sub_Categories"

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_frik_sub_cat', None, {'slug': self.slug}
# ##


# maximum of 5 friks(gigs) per users
class MyFrik(models.Model):
    frik_owner = models.ForeignKey(User, on_delete=models.CASCADE) # (owner of gig -> set maximum number of 5gigs)
    frik_title = models.CharField(max_length=150, unique=True, verbose_name='Post Title')
    frik_slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    frik_detail = models.TextField(verbose_name='Frik Detailed Description', blank=True)
    frik_desc = models.CharField(max_length=500, verbose_name='Frik Short Description', blank=True)
    frik_cat = models.ForeignKey(Category, related_name='friks', verbose_name='Category')
    frik_subcat = models.ForeignKey(SubCategory, related_name='friks', verbose_name='Sub Category')
    service_images1 = models.ImageField(upload_to='friks/', verbose_name='Frik Desc Image')
    frik_status = models.BooleanField(default=None) #choice 1 or 2 for active or inactive
    frik_price = models.IntegerField(null=True)
    skills_set = models.CharField() #list seperated by commas
    # tags = models.CharField()
    # ratings = models.CharField()

    class Meta:
        verbose_name = "My Friks"
        verbose_name_plural = "My_Friks"

    def __str__(self):
        return u'%s %s' % (self.frik_owner, self.frik_title)

    @permalink
    def get_absolute_url(self):
        return 'view_frik_detail', None, {'slug': self.slug}
    ##
    # methods for the frik model object
    # makeOrder() = a function for the user to submit offers for the user(seller_frik)
    # makeCustomOrder() = a function for the user(buyer) to submit a custom offer 4 d user(seller_frik) wit custom price
    # sendCustomOrder() = a function for the user(seller_frik) to send a custom offer 2 a specific user wit custom price
    # acceptOffer() = a function for the user(seller_frik) to accept the offer
    # rejectOffer() = a function for the user(seller_frik) to reject the offer
    # acceptCustomOffer() = a function for the user(buyer) to accept the custom offer from a user(seller_frik)
    # rejectCustomOffer() = a function for the user(buyer) to reject the custom offer from a user(seller_frik)
# ##


class MyOffers(models.Model):
    frik = models.CharField()  # linked to seller frik.title
    frik_owner = models.CharField() # set to seller frik.username
    buyer_username = models.ForeignKey(User) # linked 2 current authenticated user account)
    service_price = models.CharField() # get  frik.price if custom offer(user sets price concluded)
    delivery_period = models.DurationField() # set a delivery_period
    revisions = models.PositiveIntegerField(default=1) # revision time is set
    offer_status = models.BooleanField() # (a field of text saying active, awaiting(SellersApproval), \
                     # delivered, completed or cancelled)

    class Meta:
        verbose_name = _('plan')
        verbose_name_plural = _('plans')

    def _str_(self):
        return u'%s %s' % (self.type, self.price)

    # methods in this offer model object
    # submitOrderCompletion() = a function for the buyer to notify completion of job
    # acceptOrderCompletion() = a function for the seller to acknowledge completion of job
    # cancelOrder() = a function for the seller to cancel offer(if cant complete) or d buyer to cancel(if time elapses)
    # orderAgain() = a function to order again after order is complete and delivered
# ##


class RequestedOffers(models.Model):
    offer_request = models.CharField()  # description of request
    request_owner = models.ForeignKey(User)  # linked 2 current authenticated user account)
    request_budget = models.IntegerField()  # budget for requested offer
    delivery_period = models.DurationField()  # set a delivery_period
    requested_offer_delivered = models.BooleanField(default=False) # set to True if requested offer delivered

    class Meta:
        verbose_name = _('Requested Offer')
        verbose_name_plural = _('Requested Offers')

    def _str_(self):
        return u'%s %s' % (self.offer_request, self.request_budget)

        # methods in this offer model object
        # startRequest() = a function for the user to create and make a request for other user to see on request board
        # cancelRequest() = a function for the user to cancel and delete requested job from the request board
        # sendOffer() = a function for the user(seller) to accept and send a custom offer to the user(requester/buyer)
        # the above moves functionlity to the MyOffers methods
        # ##

# creating the user's gig table when he signs up
# @receiver(post_save, sender=User)
# def create_user_gig_table(sender, instance, created, **kwargs):
#     MyFriks.objects.create(user=instance)
# ##


# creating  the user's offers table when they sign up
# @receiver(post_save, sender=User)
# def create_user_offer_table(sender, instance, **kwargs):
#     MyOffers.object.create(user=instance)
# ##