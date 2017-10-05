# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='cmsplugin-carousel-ai',
    version='0.0.3',
    author='Anders Innovations',
    author_email='info@anders.fi',
    packages=['cmsplugin_carousel_ai', 'cmsplugin_carousel_ai.migrations', 'cmsplugin_carousel_ai.templates'],
    include_package_data=True,
    license='MIT',
    description='Image carousel plugin for Django CMS',
    install_requires=[
        'django-cms>=3.2,<3.4',
        'django-enumfields>=0.8.2',
        'django-filer>=1.2.4',
        'easy-thumbnails>=2.3',
    ],
    url='https://github.com/andersinno/cmsplugin-carousel-ai',
)
