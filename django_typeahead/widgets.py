# -*- coding: utf-8 -*-
from django import forms
from json import dumps as json_dumps


class TypeaheadInput(forms.TextInput):
    """
    Input class for typeahead-enabled widgets.
    """
    input_type = 'search'
    template_name = 'django_typeahead/input.html'
    options = None
    datasets = []

    class Media:
        """JS/CSS resources needed to render the typeahead field."""

        js = [
            'https://cdnjs.cloudflare.com/ajax/libs/corejs-typeahead/1.2.1/typeahead.bundle.min.js',
            'django_typeahead/js/typeahead.js',
        ]
        css = {'all': [
            'django_typeahead/css/typeahead.css',
        ], }

    def __init__(self, attrs={}, options={}, datasets=[]):

        # copy typeahead arguments, also allow class level declaration
        self.options = options or self.options
        self.datasets = datasets or self.datasets

        # automatically wrap dataset into list if it is singular
        if isinstance(self.datasets, dict):
            self.datasets = [self.datasets]

        # setup additional attributes for input field
        typeahead_attrs = dict(attrs) if attrs else dict()
        input_classes = typeahead_attrs.get('class', '').split(' ')

        typeahead_attrs['class'] = ' '.join(input_classes + ['typeahead'])
        typeahead_attrs['autocomplete'] = 'off'

        # initialize parent Input class
        super().__init__(typeahead_attrs)

    def to_json(self):
        """
        Custom JSON serialization logic, may be expanded with custom BloodhoundEncoder later.
        """
        json_attrs = dict(options=self.options, datasets=self.datasets)
        return json_dumps(json_attrs)

    def get_context(self, name, value, attrs):
        """
        Return widget context dictionary with additional typeahead configurations.
        """
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['tjs_config'] = self.to_json()
        return context
