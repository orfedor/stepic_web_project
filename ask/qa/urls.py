from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_paige, name='index'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<question_id>\d+)/$', views.Quest, name='question'),
    url(r'^ask/$', views.Ask, name='ask'),
    url(r'^popular/$', views.pop, name='popular'),
    url(r'^new/$', views.test, name='new')
]
