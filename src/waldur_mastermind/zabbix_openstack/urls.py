from __future__ import unicode_literals

from django.conf.urls import url

from . import views


def register_in(router):
    router.register(r'zabbix-openstack-links', views.LinkViewSet, base_name='zabbix-openstack-links')


urlpatterns = []
