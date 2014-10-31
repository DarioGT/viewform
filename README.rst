===============
django-viewform
===============

What if there is another way?

.. image:: http://i.imgur.com/3duy4OZ.gif


Template driven form rendering for data entry applications

Demo: http://forms.viewflow.io/


Template tags
=============

`viewform` built around simple concept called viewpart. `Viewpart` is
the like django template block, it has a default value and could be
overriden.  But `viewparts` are created dynamically for each form
field, allows you to redefince specific form field html render output.

Here is the example of rendering form with predefined bootstrap template,
but prepend email field with `@` sign.

.. code-block:: html

    <form method="POST">
        {% csrf_token %}
        {% viewform 'viewform/bootstrap3/form.html' form=form layout=view.layout %}
            {% viewpart form.email.field prepend %}
                 <div class="input-group-addon">@</div>
            {% endviewpart %}
        {% endviewform %}
        <button type="submit" name="_submit" class="btn btn-primary btn-lg">Submit</button>
    </form>

There is a lot of other viewparts declared in default templates. See template code for details.
If your widget is so special, just provide `{% viewpart form.my_field.field %}any html code{% endviewpart %}`

Layout
======

Simple and declarative way to specify relative fields placements and sizes. Layouts rendering details
itself are also specified in template.


See more on `demo page <http://forms.viewflow.io/>`_
