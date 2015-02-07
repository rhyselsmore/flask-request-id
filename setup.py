#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand
except ImportError:
    from distutils.core import setup, Command as TestCommand

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


# grifted from http://bit.ly/1AoDLp1
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['test_flask_request_id.py']
        self.test_suite = True

    def run_tests(self):
        from pkg_resources import _namespace_packages
        import pytest

        # Purge modules under test from sys.modules. The test loader will
        # re-import them from the build location. Required when 2to3 is used
        # with namespace packages.
        v = sys.version_info
        if v >= (3,) and getattr(self.distribution, 'use_2to3', False):
            module = self.test_args[-1].split('.')[0]
            if module in _namespace_packages:
                del_modules = []
                if module in sys.modules:
                    del_modules.append(module)
                module += '.'
                for name in sys.modules:
                    if name.startswith(module):
                        del_modules.append(name)
                map(sys.modules.__delitem__, del_modules)

            # Run on the build directory for 2to3-built code
            # This will prevent the old 2.x code from being found
            # by py.test discovery mechanism, that apparently
            # ignores sys.path..
            ei_cmd = self.get_finalized_command("egg_info")
            self.test_args = [normalize_path(ei_cmd.egg_base)]

        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='flask-request-id',
    version='0.1',
    url='http://github.com/rhyselsmore/flask-request-id',
    author='Rhys Elsmore',
    author_email='me@rhys.io',
    description='Extract yourself some Request IDs.',
    long_description='Extract yourself some Request IDs. See https://github.com/rhyselsmore/flask-request-id',
    py_modules=['flask_request_id'],
    license=open('LICENSE').read(),
    package_data={'': ['LICENSE']},
    zip_safe=False,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    platforms='any',
    install_requires=[
        'Flask>=0.7',
        'wsgi-request-id>=0.2'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
