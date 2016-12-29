from django.conf.urls import include, url
from afrikalmarket import views as afrikalmarket_views

urlpatterns = [
    url(r'^', afrikalmarket_views.index, name='index'),
]
