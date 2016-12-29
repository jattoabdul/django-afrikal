# django-afrikal
an online service market(a fiverr clone)


 Its an application where ->
 - All users can create a profile
 - All users can create a frik(frik is like a Basket of services rendered) where we store information about the friks -> user can have not more than 7 friks).
 - All users(buyers state) can order for any user's frik(services). Ordering requires user(seller)'s approval/acceptance.
 - All users can make request and wait for any user's frik to send you and offer. requester user approves/accepts the offer and makes payment.
 - All users  can add,edit and delete their friks and he can create an offer for "the default price" or a
       "a custom offer for the user(buyer state) with a custom price".
 - All registered users who registered on the site can communicate via chat.
 - All registered users can view their profile&Friks and other users profile&Friks.
 - only owner of profile can update and delete profile (NB: if delete profile, the whole account is deleted)
 - only owner of Friks can add, update, activate, deactivate and delete Friks 
# end##


# workflow of site

- signup(if new user) NB: anonymouse users can view home page but cannot do anyother thing except they register
- signin (with new credentials)
- update profile
- create and activate Frik (if you want to create Friks to sell with)
- search nd request a Frik (if youwant to get a service from created friks)
- make order,->wait for acceptance,->make payment,->get service,->get completion notif,->ascertain completion notif,->congrats(reorder)
- make request,->wait for offer,->accept offer->make payment,->get service,->get completion notif,->ascertain completion notif,->congrats(reorder)


# TODOS
-> + means done. = means in progress
- add user registration and profile management functionality +
- add frik management functionality =
- add blog functionality +
- add chat functionality
- add market payment functionality (stripes payment method)
- add request management functionality
- add forum functionality
- others