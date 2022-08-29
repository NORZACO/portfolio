from django.contrib import admin
from django.urls import path


#from betaleapp.viewings import home
import bloge.viewings.home


from django.contrib import admin
from django.urls import path


from bloge.viewings import home





#  /Users/mwamuzishadrick/Localsites/payement/betaleapp/urls.py -->
urlpatterns = [
    path('', home.homepage, name='index'),
    path('details/<int:job_id>', home.detailspage, name="details"),
    #path('details/', home.details_page, name="details"),
]
