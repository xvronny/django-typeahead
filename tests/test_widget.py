# -*- coding: utf-8 -*-
from json import loads as json_loads
from django.test import TestCase

from django_typeahead.widgets import TypeaheadInput


class TestWidget(TestCase):

    def test_default_constructor(self):
        widget = TypeaheadInput()
        self.assertEqual(None, widget.options)
        self.assertEqual([], widget.datasets)

    def test_single_dataset(self):
        options = dict(hint=True, highlight=True, minLength=1)
        dataset = dict(name='states')
        widget = TypeaheadInput(options=options, datasets=dataset)
        self.assertEqual(options, widget.options)
        self.assertEqual([dataset], widget.datasets)

    def test_multiple_datasets(self):
        options = dict(hint=True, highlight=False, minLength=3)
        dataset_a = dict(name='municipalities')
        dataset_b = dict(name='counties')
        widget = TypeaheadInput(options=options, datasets=[dataset_a, dataset_b])
        self.assertEqual(options, widget.options)
        self.assertEqual(dataset_a, widget.datasets[0])
        self.assertEqual(dataset_b, widget.datasets[1])

    def test_context(self):
        options = dict(hint=True, highlight=True, minLength=1)
        dataset_a = dict(name='municipalities')
        dataset_b = dict(name='counties')
        widget = TypeaheadInput(options=options, datasets=[dataset_a, dataset_b])
        context = widget.get_context('test', 'yes', dict())

        # verify result of contextualization
        attr_config = json_loads(context['widget']['attrs']['tjs_config'])
        self.assertEqual(options, attr_config['options'])
        self.assertEqual(dataset_a, attr_config['datasets'][0])
        self.assertEqual(dataset_b, attr_config['datasets'][1])
