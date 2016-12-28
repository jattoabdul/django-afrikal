# I am using django-userena application to handle user-registration, user-profile and log-in. Now I'm writing an
# application where -
# *All users can create a profile (buyer or seller)
# *A user(seller) can create a gig(gig is like a profile(service rendered) where we store information about the gig and
#  a user can have upto 5 gig).
# *Other users(buyers) can order for any gig(service). Ordering requires seller's approval.
# *Only sellers  can add,edit and delete the gigs page and he can create an offer for "the default price" or a
# "custom order for the buyers order on a gig" .
# *All registered users(buyers and sellers) who registered on the site can communicate via chat.
# *All registered users(buyers and sellers) can view their profile and other gigs profile.
#
# How should I architect this application? setting my groups(sellers and buyers) and permissions.
