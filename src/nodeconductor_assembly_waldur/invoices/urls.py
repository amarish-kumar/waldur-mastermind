from __future__ import unicode_literals

from nodeconductor_assembly_waldur.invoices import views


def register_in(router):
    router.register(r'invoices', views.InvoiceViewSet, base_name='invoice')