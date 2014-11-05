import extra_views
from django.http import HttpResponseRedirect
from django.template import Template

from viewform import Layout, Inline, Row, Column
from ..django_forms import LayoutMixin
from .models import Shipment, ShipmentItem


class FormsetView(LayoutMixin,
                  extra_views.NamedFormsetsMixin,
                  extra_views.CreateWithInlinesView):
    model = Shipment

    class ItemInline(extra_views.InlineFormSet):
        model = ShipmentItem
        fields = ['name', 'quantity']

    layout = Layout(
        Row(Column('name', 'city'),
            Column('address_line1', 'address_line2')),
        Inline('Items', ItemInline)
    )

    template_bootstrap = Template("""""")

    template_foundation = Template("""""")

    def forms_valid(self, form, inlines):
        return HttpResponseRedirect(self.get_success_url())
