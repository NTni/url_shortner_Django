from django.conf.urls import url

from.import views


urlpatterns = [
    #/marvel/
    url(r'^$', views.avengers,name='avengers'),
    #/marvel/hero/
    url('hero/',views.hero,name='hero' ),
    #/marvel/villain/
    url('villain/',views.villain,name='villain'),

]