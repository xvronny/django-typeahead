Walkthrough
===========

This section translates the `first example (basics) <https://twitter.github.io/typeahead.js/examples/#the-basics>`_ sample from Typeahead.js `examples page <https://twitter.github.io/typeahead.js/examples>`_.

Using ``TypeaheadInput``
------------------------

The input widget ``TypeaheadInput`` would be used as a widget in Django forms.

.. code-block:: python

    from django import forms
    from bootstrap_typeahead.widgets import TypeaheadInput

    class StateForm(forms.Form):
        query = forms.CharField(
            widget=TypeaheadInput(
                options={
                  'hint': True,
                  'highlight': True,
                  'minLength': 1
                },
                datasets={
                  'name': 'states',
                  'source': 'substringMatcher(states)',
                }
            )
        )

The ``options`` and ``datasets`` argument will be passed to the JavaScript typeahead instance,
and are documented and demonstrated here:

* `Typeahead Documentation <https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md>`_
* `Bloodhound Documentation <https://github.com/twitter/typeahead.js/blob/master/doc/bloodhound.md>`_
* `Interactive Demo <https://twitter.github.io/typeahead.js/examples/>`_

Creating a Template
-------------------

The initialization of suggestions list should be added to the page - in this case we are using snippet from `basic example <https://twitter.github.io/typeahead.js/examples/#the-basics>`_ from Typeahead.js demo page.

.. code:: Django

    {% load bootstrap4 %}

    {# Load CSS and JavaScript #}
    {% bootstrap_css %}

    {% block extra_css %}
    {{ form.media.css }}
    {% endblock %}

        <form method="post" role="form">
        {% csrf_token %}
        {% bootstrap_form form %}
          <div class="form-group">
            <input type="submit" value="Submit" class="btn btn-primary" />
          </div>
        </form>

    {% bootstrap_javascript jquery='full' %}

    {% block extra_js %}
        <script type="text/javascript">
        var substringMatcher = function(strs) {
          return function findMatches(q, cb) {
            var matches, substringRegex;

            // an array that will be populated with substring matches
            matches = [];

            // regex used to determine if a string contains the substring `q`
            substrRegex = new RegExp(q, 'i');

            // iterate through the pool of strings and for any string that
            // contains the substring `q`, add it to the `matches` array
            $.each(strs, function(i, str) {
              if (substrRegex.test(str)) {
                matches.push(str);
              }
            });

            cb(matches);
          };
        };

        var states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
          'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii',
          'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
          'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
          'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
          'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
          'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
          'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
        ];
        </script>
        {{ form.media.js }}

    {% endblock %}

Here we use `django-bootstrap4 <https://github.com/zostera/django-bootstrap4>`_ but you can create your HTML forms manually.
