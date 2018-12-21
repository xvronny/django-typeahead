# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.urls import reverse
from django.test import TestCase


class ViewTestCase(TestCase):

    def test_assertion(self):
        response = True
        self.assertEquals(True, response)
