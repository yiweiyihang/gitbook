#Python decode()方法


#描述
Python decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码。

#语法

decode()方法语法：
```
str.decode(encoding='UTF-8',errors='strict')
```

#参数
- encoding -- 要使用的编码，如"UTF-8"。
- errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

#返回值
该方法返回解码后的字符串。

#实例
以下实例展示了decode()方法的实例：

```
#!/usr/bin/python

str = "this is string example....wow!!!";
str = str.encode('base64','strict');

print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')
```

以上实例输出结果如下：

```
Encoded String: dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE=

Decoded String: this is string example....wow!!!
```