# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name='cmsplugin-carousel-ai',
    version='0.0.1',
    author='Anders Innovations',
    author_email='info@anders.fi',
    packages=['cmsplugin_carousel_ai', 'cmsplugin_carousel_ai.migrations', 'cmsplugin_carousel_ai.templates'],
    include_package_data=True,
    license='MIT',
    long_description=open('README.md').read(),
    description='Image carousel plugin for Django CMS',
    install_requires=open('requirements.txt').readlines(),
    url='https://github.com/andersinno/cmsplugin-carousel-ai',
)
