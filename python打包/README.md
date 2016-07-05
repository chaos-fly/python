# python 打包

## 文档
- [python 管理工具小结](https://github.com/stanzgy/wiki/blob/master/openstack/python-packaging.md)

- [Python Packaging 手册](https://packaging.python.org/distributing/#manifest-in)

- [setuptools 手册](https://setuptools.readthedocs.io/en/latest/setuptools.html)

## python 虚拟环境virtualenv
- 安装虚拟环境工具 `pip install virtualenv`

- 执行`virtualenv env1`, 在当前目录创建最小python环境（包含setuptools，pip等）

- 切换到虚拟环境`source env1/bin/activate`

## setuptools 示例文件
- python打包，需要在包目录下创建一个`setup.py`文件，
- 当前目录下的所有package（包含__init__.py的目录）都会被打进包
- package`world` 因为被setup.py过滤，所以不会打入包
- 非`.py`文件默认不会打包，如果需要打包，可以通过`MANIFEST.in`配置
