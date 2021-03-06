from django.conf.urls import patterns, url
from django.views import generic

from tests import forms
from tests.examples.views import FormsetView


urlpatterns = patterns(
    '',
    url(r'^$', generic.RedirectView.as_view(url='/foundation/basic/')),
    url(r'^bootstrap/basic/$', generic.FormView.as_view(
        form_class=forms.BasicElementsForm,
        success_url='/bootstrap/basic/',
        template_name="bootstrap.html")),
    url(r'^bootstrap/fieldset/$', generic.FormView.as_view(
        form_class=forms.FieldsetForm,
        success_url='/bootstrap/fieldset/',
        template_name="bootstrap.html")),
    url(r'^bootstrap/complexlayout/$', generic.FormView.as_view(
        form_class=forms.ComplexLayoutForm,
        success_url='/bootstrap/complexlayout/',
        template_name="bootstrap.html")),
    url(r'^bootstrap/datetime/$', generic.FormView.as_view(
        form_class=forms.DatetimePickersForm,
        success_url='/bootstrap/datetime/',
        template_name="bootstrap.html")),
    url(r'^bootstrap/formset/$', FormsetView.as_view(
        success_url='/bootstrap/formset/',
        template_name="bootstrap.html")),
    url(r'^foundation/basic/$', generic.FormView.as_view(
        form_class=forms.BasicElementsForm,
        success_url='/foundation/basic/',
        template_name="foundation.html")),
    url(r'^foundation/fieldset/$', generic.FormView.as_view(
        form_class=forms.FieldsetForm,
        success_url='/foundation/fieldset/',
        template_name="foundation.html")),
    url(r'^foundation/complexlayout/$', generic.FormView.as_view(
        form_class=forms.ComplexLayoutForm,
        success_url='/foundation/complexlayout/',
        template_name="foundation.html")),
    url(r'^foundation/datetime/$', generic.FormView.as_view(
        form_class=forms.DatetimePickersForm,
        success_url='/foundation/datetime/',
        template_name="foundation.html")),
    url(r'^foundation/formset/$', FormsetView.as_view(
        success_url='/foundation/formset/',
        template_name="foundation.html")),
)
