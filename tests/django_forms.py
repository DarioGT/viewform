import django
from django.forms import *  # NOQA


class DemoFormMixin(object):
    def source(self):
        import inspect
        import itertools

        lines = inspect.getsourcelines(self.__class__)[0]
        lines = [x for x in itertools.takewhile(lambda x: not x.strip().startswith('template'), lines)]
        return ''.join(lines)


class Form(DemoFormMixin, django.forms.Form):
    pass
