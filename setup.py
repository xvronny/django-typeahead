import os
import re

from setuptools import find_packages, setup

# Read version from app
with open("django_typeahead/__init__.py", "rb") as f:
    VERSION = str(re.search('__version__ = "(.+?)"', f.read().decode("utf-8")).group(1))

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-typeahead',
    version=VERSION,
    packages=find_packages(),
    description='Django app to add Typeahead.js based input elements.',
    long_description=README,
    url='https://github.com/xvronny/django-typeahead/',
    download_url='https://github.com/xvronny/django-typeahead.git',
    license='MIT License',
    include_package_data=True,
    install_requires=[
        'Django>=2.0'
    ],
    zip_safe=False,
    author='Ronny Hendrawan',
    author_email='ronny.hendrawan@gmail.com',
    keywords='django-typeahead',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
