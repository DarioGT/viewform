from django.conf.urls import patterns, url
from integration.views import OrderView
from unit.views import AllElemFormView


urlpatterns = patterns(
    '',
    url(r'^order/$', OrderView.as_view()),
    url(r'^elements/$', AllElemFormView.as_view()))
