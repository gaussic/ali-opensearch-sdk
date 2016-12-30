#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='opensearch-sibbay',
    version='2.1.0',
    packages=find_packages(),
    keywords=('OpenSearch SDK', 'Aliyun for Sibbay'),
    description='Python SDK for OpenSearch of Ali Cloud',
    license='Apache License Version 2.0',
    url='https://github.com/yanheven/ali-opensearch-sdk',
    author='Yan Haifeng(颜海峰)',
    author_email='yanheven@qq.com',

    include_package_data=True,
    platforms='any',
    install_requires=['requests', 'six'],
    classifiers=['Operating System :: MacOS',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.5']
)
