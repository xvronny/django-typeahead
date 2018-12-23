Getting Started
===============

Requirements
------------

* Python >= 3.5
* Django >= 2.1
* jquery >= 1.9


Installation
------------

1. Install using pip:

   ``pip install django-typeahead``

2. Add ``bootstrap_typeahead`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file:

   .. code-block:: python

      INSTALLED_APPS = [
          # ...
          'bootstrap_typeahead',
      ]

   .. warning:: This installation instruction assumes you have ``jQuery`` and Bootstrap JS/CSS files present
      in your template and you are using ``form.media`` in your django template. If not you should checkout our
      `usage instructions <usage>`__ which covers almost everything you need to get the widget running.
