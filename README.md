# django-typeahead

This package contains a Django widget for autocomplete search functionality using Twitter's [typeahead.js ](https://github.com/twitter/typeahead.js) library.

## Install

    pip install django-typeahead

Add `bootstrap_typeahead` to the list of INSTALLED_APPS in your settings.py file.

    INSTALLED_APPS = [
        # ...
        'bootstrap_typeahead',
    ]

This installation instruction assumes you have jQuery already present in your page.

## Example

#### forms.py

```python
from bootstrap_typeahead.widgets import TypeaheadInput
from django import forms

class SearchForm(forms.Form):
    todo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    autocomplete = forms.CharField(
        widget=TypeaheadInput(
            options={
              'hint': True,
              'highlight': True,
              'minLength': 1
            },
            datasets={
              'name': 'states',
              'source': substringMatcher(states)
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
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="{% static 'contrib/bootstrap.css' %}">
    <link rel="stylesheet" href="{% static 'contrib/font-awesome.min.css' %}">
    <script src="{% static 'contrib/bootstrap.js' %}"></script>
  </head>
  <body>
    <form method="post" role="form">
      {{ form|bootstrap }}
      {% csrf_token %}
      <div class="form-group">
        <input type="submit" value="Submit" class="btn btn-primary" />
      </div>
    </form>
  </body>
</html>
```

Here we assume you're using [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) or
[django-jinja-bootstrap-form](https://github.com/samuelcolvin/django-jinja-bootstrap-form) but you can
create your HTML forms manually.

## Requirements

* Python >= 3.4
* Django >= 2.0
* jquery >= 1.7.1
