#5-1 调用函数


Python内置了很多有用的函数，我们可以直接调用。

要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：

http://docs.python.org/3/library/functions.html#abs

也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。

调用abs函数：

	>>> abs(100)
	100
	>>> abs(-20)
	20
	>>> abs(12.34)
	12.34
调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个：

	>>> abs(1, 2)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: abs() takes exactly one argument (2 given)
如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型：

	>>> abs('a')
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: bad operand type for abs(): 'str'
而max函数max()可以接收任意多个参数，并返回最大的那个：

	>>> max(1, 2)
	2
	>>> max(2, 3, 1, -5)
	3
##数据类型转换

Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：

	>>> int('123')
	123
	>>> int(12.34)
	12
	>>> float('12.34')
	12.34
	>>> str(1.23)
	'1.23'
	>>> str(100)
	'100'
	>>> bool(1)
	True
	>>> bool('')
	False

函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

	>>> a = abs # 变量a指向abs函数
	>>> a(-1) # 所以也可以通过a调用abs函数
	1

##练习

请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

	# -*- coding: utf-8 -*-
	
	n1 = 255
	n2 = 1000
	
	print(???)


##小结

调用Python的函数，需要根据函数定义，传入正确的参数。如果函数调用出错，一定要学会看错误信息，所以英文很重要！

##参考源码

- 本地

[call_func.py](../code/chapter5/5-1-call_func.py)

- github

[call_func.py](https://github.com/michaelliao/learn-python3/blob/master/samples/function/call_func.py)