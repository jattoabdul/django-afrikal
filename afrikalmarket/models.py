from django.db import models

# Create your models here.

# maximum of 5 gigs per users(seller only)
# class MyGigs(models.Model):
#   service_seller = models.ForeignKey(User, on_delete=models.CASCADE)(owner of gig)
#   service_title
#   service_desc
#   service_cat
#   service_subcat
#   service_images1
#   service_images2
#   service_images3
#   service_plan
#   tags
#   ratings
#   ##
#   methods fot the gig model
#   makeOrder() = a function for the buyer to submit offers for the seller
#   makeCustomOrder() = a function for the buyer to submit a custom offer for the seller with price agreed upon
#   sendCustomOrder() = a function for the seller to send a custom offer to a specific buyer based on the price agreed
#   acceptOrder() = a function for the seller to accept the offer
#   rejectOffer() = a function for the seller to reject the offer
#   acceptCustomOrder() = a function for the buyer to accept the custom offer
#   rejectCustomOffer() = a function for the buyer to reject the custom offer
# ##

# class Category(models.Model):
#   cat = model.CharField()

# class SubCateogory
#   sub_cat = model.CharField()
# ##

# class Plan(models.Model):
#   type = (choice from basic, premium, custom)
#   price
#   delivery_period(days)
#   revisions
#   skills_set
# ##

# class MyOffers(models.Model):
#   seller_username = (models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#                       ->linked to user with seller account role)
#   seller_gig = (models.ForeignKey(settings.Auth_user_model)linked to seller gig)
#   buyer_username = (models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#                      ->linked to user with  buyer account role)
#   service_plan = plan
#   service_price = plan.price (if service plan is custom, buyer adds bargained price)
#   delivery_period = plan.delivery_period
#   revisions = plan.revision
#   offer_status = (a field of text saying completed or in progress or cancelled)
#   methods in this offer model object
#   submitOrderCompletion() = a function for the buyer to notify completion of job
#   acceptOrderCompletion() = a function for the seller to acknowledge completion of job
#   cancelOrder() = a function for the seller to cancel offer(if cant complete) or the buyer to cancel(if time elapses)
# ##


