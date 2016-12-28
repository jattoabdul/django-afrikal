from django.conf.urls import include, url
from afrikalmarket import views

urlpatterns = [
    url(r'^', views.index, name='index'),
]
