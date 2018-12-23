# -*- coding: utf-8 -*-
from django import forms
from json import JSONEncoder


class Bloodhound(object):
    """
    Special representation for Bloodhound lookahead engine.
    """

    class Tokenizer(object):
        """

        """
        whitespace = None

    tokenizer = Tokenizer()

    keywords = ['datumTokenizer', 'queryTokenizer', 'initialize', 'identify', 'sufficient',
                'sorter', 'local', 'prefetch', 'remote']

    def __init__(self, *args, **kwargs):
        self.arguments = dict()
        if args:
            for i, value in enumerate(args):
                key = Bloodhound.keywords[i]
                self.argument[key] = value
        if kwargs:
            for key in Bloodhound.keywords:
                if key in kwargs:
                    self.argument[key] = kwargs[key]

    def to_eval_string(self):
        pass


class BloodhoundEncoder(JSONEncoder):
    """
    Custom Bloodhound-aware JSONEncoder class.
    """

    def default(self, obj):
        if isinstance(obj, Bloodhound):
            return obj.__json__()
        return JSONEncoder.default(self, obj)
