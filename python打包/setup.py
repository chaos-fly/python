#!/usr/bin/env python
#-*- coding:utf8 -*-
from setuptools import setup, find_packages

setup(
    name='hellow',
    version = '1.0.0',

    description = 'my hellow pkg',
    author='grj',
    author_email='',
    url='-',

    # 自动寻找当前目录下的所有packages（包含__init__.py 的目录)
    # exclude 过滤某些目录
    packages = find_packages(exclude=['world']),

    # 依赖包
    install_requires=[
        'redis>=2.8',
        'pyinotify==0.9.6',
    ],
    dependency_links = [
        'http://dl.vip.yy.com/myback/pyinotify-0.9.6.tar.gz#egg=pyinotify-0.9.6',
    ],

    # 包里面的附加文件文件，默认只打包.py文件
    # 用了include_package_data 这个选项貌似失效了
    #package_data = {
    #    'hellow' : ['abc.txt'],
    #},

    # 这种方法中包内所有文件指通过MANIFEST.in声明的
    include_package_data = True,

    # 在site-packages里面以文件夹的形式安装
    zip_safe = False,

    # 创建可执行脚本
    entry_points = {
        'console_scripts' : ['funi-test=hellow.t1:t1'],
    }
)

