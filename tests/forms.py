from django.template import Template
from viewform import Layout, Row, Fieldset, Column, Span2, Span3
import django_forms as forms


CITY_CHOICES = (('Paris', 'Paris'),
                ('London', 'London'),
                ('New York', 'New York'))


GENDER_CHOICES = (('Male', 'Male'),
                  ('Female', 'Female'),
                  ('Facebook approved', 'Facebook approved'),
                  ('Other', 'Other'))


TAG_CHOICES = (('1', 'One'), ('2', 'Two'), ('3', 'Three'))


VENDOR_CHOICES = (
    (1, 'Magna Phasellus Dolor Incorporated'),
    (2, 'Fames Ac Turpis Inc.'),
    (3, 'Eu Eros Institute'),
    (4, 'Suspendisse Sagittis Associates'))


PRODUCT_TYPE_CHOICES = (
    ('ETM', 'Et magnis'),
    ('VRH', 'Vivamus rhoncus'),
    ('EGL', 'Egestas ligula'),
    ('NLC', 'Nulla. Cras'))


class BasicElementsForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    password = forms.CharField(widget=forms.PasswordInput)

    layout = Layout(
        Row('first_name', 'last_name'),
        Row('email', 'date_of_birth'),
        'password')

    template_bootstrap = Template("""
    {% viewpart form.email.field prepend %}
        <div class="input-group-addon">@</div>
    {% endviewpart %}
    """)


class FieldsetForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()

    address_line1 = forms.CharField(max_length=150, label="Street")
    address_line2 = forms.CharField(max_length=150, label="Home, Flat")
    city = forms.ChoiceField(choices=CITY_CHOICES)

    layout = Layout(
        Row(Fieldset("Personal details", "first_name", "last_name", "email"),
            Fieldset("Address", "address_line1", "address_line2", "city", span_columns=3)))

    template_bootstrap = Template("""
    {% viewpart form.email.field add_control_class %}input-lg{% endviewpart %}
    {% viewpart form.address_line1.field add_control_class %}input-lg{% endviewpart %}
    """)


class ComplexLayoutForm(forms.Form):
    product_name = forms.CharField()
    tags = forms.MultipleChoiceField(choices=TAG_CHOICES)

    vendor = forms.ChoiceField(choices=VENDOR_CHOICES)
    product_type = forms.ChoiceField(choices=PRODUCT_TYPE_CHOICES)

    sku = forms.CharField()
    stock_level = forms.IntegerField()
    cost_price = forms.DecimalField(max_value=100, min_value=10, max_digits=5, decimal_places=2)
    wholesale_price = forms.DecimalField(max_value=100, min_value=10, max_digits=5, decimal_places=2)
    retail_price = forms.DecimalField(max_value=100, min_value=10, max_digits=5, decimal_places=2)

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    product_description = forms.Textarea()

    layout = Layout(
        Fieldset("Add to inventory",
                 Row(Span3('product_name'), 'tags'),
                 Row('vendor', 'product_type'),
                 Row(Column('sku',
                            'stock_level',
                            span_columns=5),
                     'gender'),
                 Row('cost_price', Span2('wholesale_price'), 'retail_price')))

    template_bootstrap = Template("""
    {% viewpart form.sku.field append %}
        <div class="input-group-addon">.##</div>
    {% endviewpart %}
    {% viewpart form.stock_level.field append %}
        <div class="input-group-addon">.00</div>
    {% endviewpart %}
    """)
