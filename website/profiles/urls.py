from django.conf.urls import url
from . import views

app_name ='profiles'

urlpatterns = [
    # /profile/
    url(r'^$', views.index, name='index'),

    # # /profile/
    # url(r'^program_detail/(?P<program_id>[0-9]+)/$', views.program_detail, name='program_detail'),
    #
    # # /profile/
    # url(r'^program_detail/$', views.program_detail, name='program_detail'),
    #
    # # /profile/
    # url(r'^team_detail/(?P<team_id>[0-9]+)/$', views.team_detail, name='team_detail'),
    #
    # # /profile/
    # url(r'^player_detail/(?P<player_id>[0-9]+)/$', views.player_detail, name='player_detail'),

    # /profile/
    #url(r'^team/$', views.detail, name='team_detail'),

    # /profile/
    #url(r'^player/$', views.detail, name='player_detail'),

    # /profile/
    #url(r'^coach/$', views.detail, name='coach_detail'),

]
