from . import views
from django.urls import path
urlpatterns = [
    path('',views.hello,name='hello'),
    #path('',views.arithmetic,name='arithmetic'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('thank/',views.thank,name='thank'),
    path('operations/',views.operations,name='operations'),


]