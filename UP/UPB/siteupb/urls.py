from django.urls import path
from django.contrib import admin
from . import views
urlpatterns =[
    path('', views.index, name= 'index'),
    path('contact', views.contact, name= 'contact'),
    path('about', views.about, name ='about'),
    path('renseignement', views.renseigne, name= 'renseigne'),
    path('srakadjan#@5253/', admin.site.urls, name='admin:index'),

]