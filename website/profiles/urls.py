from django.conf.urls import url
from . import views

app_name ='profiles'

urlpatterns = [
    # /profile/
    url(r'^$', views.index, name='index')

    # # /profile/
    # url(r'^program_detail/(?P<program_id>[0-9]+)/$', views.program_detail, name='program_detail'),
    #

]