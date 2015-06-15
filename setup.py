#coding=utf8

from setuptools import setup


entry_points = [
    'whelper = walis.helper:helper',
    "wthrift = walis.thrift.client:jvs_test",
]


setup(
    name='walis',
    version='1.0.0',
    packages=['walis'],
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": entry_points},
    install_requires=open('requirements.txt').readlines()
)
