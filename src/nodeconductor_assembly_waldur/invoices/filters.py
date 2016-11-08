import django_filters

from nodeconductor.core.filters import UUIDFilter

from . import models


class InvoiceFilter(django_filters.FilterSet):
    customer_uuid = UUIDFilter(name='customer__uuid')
    state = django_filters.MultipleChoiceFilter(choices=models.Invoice.States.CHOICES)

    class Meta(object):
        model = models.Invoice
        fields = ('customer_uuid', 'state', 'year', 'month')
