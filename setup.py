import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='thinkami_reusable_app_sample',
    version='0.1',
    packages=['thinkami_reusable_app'],
    include_package_data=True,
    description='reusable django app sample',
    long_description=README,
    url='https://github.com/thinkAmi-sandbox/Django_reusable_form_sample',
    author='thinkAmi',
    author_email='dev.thinkami@gmail.com',
    license='Public Domain',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: Public Domain',
        'Programming Language :: Python :: 3.4',
    ],
)