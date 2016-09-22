from django.conf.urls import url
from . import views

urlpatterns = [
    # /profile/
    url(r'^$',views.index, name='index'),

    # /profile/
    url(r'^(?P<group_id>[0-9]+)/$',views.detail, name='detail'),
]
