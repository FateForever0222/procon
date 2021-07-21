from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='proconindex'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('ProConWeb.html', views.procon_web, name='ProConWeb'),
    path('ProConJava.html', views.procon_java, name='ProConJava'),
    path('ProCon-python-userguide-V1.0.html', views.procon_python, name='ProCon-python-userguide'),
    path('sign.html', views.sign, name='sign'),
    path('result.html', views.result, name='result'),
    path('calculate', views.calculate, name='calculate'),
    path('signin', views.signin, name='signin'),
]