from django.template import Template, Context
from django.test import TestCase


class TestRenderElementes(TestCase):
    def render(self, template_content, form, layout):
        template = Template(template_content)
        return template.render(Context({'form': form, 'layout': layout}))

    def test_render_bootstrap(self):
        TEMPLATE = """
        {% load viewform %}
        {% viewflow 'viewform/bootstrap3/form.html' form=form layout=layout %}
        {% endviewform %}
        """
        self.render(TEMPLATE)

    def _test_render_foundation(self):
        TEMPLATE = """
        {% load viewform %}
        {% viewflow 'viewform/foundation/form.html' form=form layout=layout %}
        {% endviewform %}
        """
        self.render(TEMPLATE)
