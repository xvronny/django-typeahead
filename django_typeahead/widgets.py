from django import forms


class TypeaheadInput(forms.TextInput):
    """
    Typeahead input class for widgets of this package.
    """
    input_type = 'search'
    template_name = 'django_typeahead/input.html'

    class Media:
        """JS/CSS resources needed to render the typeahead field."""

        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/corejs-typeahead/1.2.1/typeahead.bundle.min.js',
            'django_typeahead/js/typeahead.js',
        )
        css = {'all': (
            'django_typeahead/css/typeahead.css',
        ), }

    def __init__(self, attrs={}):
        typeahead_attrs = dict(attrs)

        input_class = typeahead_attrs.get('class') or ''
        typeahead_attrs['class'] = input_class + ' typeahead'
        typeahead_attrs['autocomplete'] = 'off'

        super().__init__(typeahead_attrs)
