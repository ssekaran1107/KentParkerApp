from django.conf.urls import url
from . import views

import django.contrib.auth.views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^kentparker$',views.home),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', django.contrib.auth.views.logout_then_login, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^login_google/(?P<email>.*)$', views.login_google, name='login_google'),
    url(r'^login_facebook/(?P<userid>.*)$', views.login_facebook, name='login_facebook'),
    url(r'^profile/(?P<name>.*)$', views.profile),
    url(r'^get_photo/(?P<name>.*)$',views.get_photo,name='get_photo'),
    url(r'^edit_profile/(?P<name>.*)$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/(?P<name>.*)$', views.change_password, name='change_password'),
    url(r'^favorite/(?P<name>.*)$',views.favorite, name='favorite'),
    url(r'^confirm_registration/(?P<name>.*)/(?P<token>.*)$',views.confirm_registration,name='confirm_registration'),
    url(r'^request_reset_password$',views.request_reset_password,name='request_reset_password'),
    url(r'^reset_password/(?P<name>.*)/(?P<token>.*)$',views.reset_password,name='reset_password'),
    # newsmaker related urls
    url(r'^create_pitch$', views.create_pitch, name='create_pitch'),
    url(r'^manage_pitch$', views.manage_pitch, name='manage_pitch'),
    # media_outlet
    url(r'^manage_journalists$', views.manage_journalists, name='manage_journalists'),
    # journalist related urls
    url(r'^journalist/(?P<tags>.*)$', views.filter_pitch, name='filter_pitch'),
]
