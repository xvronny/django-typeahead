
# Typeahead.js for Django


[![Continuous Integration Status](https://travis-ci.org/xvronny/django-typeahead.svg?branch=master)](https://travis-ci.org/xvronny/django-typeahead)
[![Coverage Status](https://coveralls.io/repos/github/xvronny/django-typeahead/badge.svg?branch=master)](https://coveralls.io/github/xvronny/django-typeahead?branch=master)
[![Latest PyPI version](https://img.shields.io/pypi/v/django-typeahead.svg)](https://pypi.python.org/pypi/django-typeahead)

Twitter's [typeahead.js ](https://github.com/twitter/typeahead.js) integration for Django.


Goal
----

The goal of this package is to seamlessly integrate Typeahead.js with Django and other django libraries.


Requirements
------------

* Python >= 3.4
* Django >= 2.0
* jquery >= 1.9


Installation
------------

    pip install django-typeahead

Add `bootstrap_typeahead` to the list of INSTALLED_APPS in your settings.py file.

    INSTALLED_APPS = [
        # ...
        'bootstrap_typeahead',
    ]

This installation instruction assumes you have jQuery already present in your page.


Example
-------

#### forms.py

```python
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
```

The `options` and `datasets` argument will be passed to the JavaScript typeahead instance,
and are documented and demonstrated here:

* [Typeahead Docs](https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md) and [Bloodhound Docs](https://github.com/twitter/typeahead.js/blob/master/doc/bloodhound.md)
* [Interactive Demo](https://twitter.github.io/typeahead.js/examples/)

#### template.html

```html
{% load bootstrap4 %}

{# Load CSS and JavaScript #}
{% bootstrap_css %}

{% block extra_css %}
{{ form.media.css }}
{% endblock %}

    <form method="post" role="form">
      {{ form|bootstrap }}
      {% csrf_token %}
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
```

Here we use [django-bootstrap4](https://github.com/zostera/django-bootstrap4) to translate [the basics](https://twitter.github.io/typeahead.js/examples/#the-basics) in Typeahead.js [examples page](https://twitter.github.io/typeahead.js/examples) but you can create your HTML forms manually.


Bugs and Suggestions
--------------------

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/xvronny/django-typeahead/issues
