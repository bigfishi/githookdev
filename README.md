# githookdev
- [如何自定义Git Hooks / 钩子目录？](https://www.jianshu.com/p/38a8e29dde21)
	- 在git项目根目录创建 tools/hooks，在里面创建对应的钩子文件，比如提交前检查 pre-commit
	- git config core.hooksPath tools/hooks
- 使用python脚本
	- 将Python27 复制到 tools目录下，在tools/hooks/创建Python脚本文件pre-commit.py，然后修改tools/hooks/pre-commit如下
	```
	#!/bin/sh
	echo "start pre-commit python script."
	# invoke python
	./tools/Python27/python.exe ./tools/hooks/pre-commit.py
	```
	- 最简单的pre-commit.py，需要注意最后的sys.exit(1)代表返回值为1，返回值为1时不能提交，返回值为0才可以提交。不过pre-commit可以通过`git commit --no-verify`跳过验证
	```
	#!/usr/local/bin/python
	import sys, os
	print "yo! this is the pre-commit hook from user defined hook"
	sys.exit(1)
	```
- python utf-8
	- [UTF-8 编码格式(python)](https://blog.csdn.net/weixin_45459224/article/details/97514799)
		- 文件第一行 `# -*- coding: utf-8 -*-`
- [【python】print输出的格式化](https://blog.csdn.net/eidolon_foot/article/details/136103228)
	```python
		print("Hello, {}. You are {} years old.".format(name, age))
	```