from django.conf.urls import patterns, url
from django.views import generic

from tests import forms

urlpatterns = patterns(
    '',
    url(r'^$', generic.TemplateView.as_view(template_name="index.html")),
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
)
