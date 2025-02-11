#Python time strptime()方法

#描述
Python time strptime() 函数根据指定的格式把一个时间字符串解析为时间元组。

#语法
strptime()方法语法：

```
time.strptime(string[, format])
```

#参数
- string -- 时间字符串。
- format -- 格式化字符串。

#返回值
返回struct_time对象。

#说明
python中时间日期格式化符号：

- %y 两位数的年份表示（00-99）
- %Y 四位数的年份表示（000-9999）
- %m 月份（01-12）
- %d 月内中的一天（0-31）
- %H 24小时制小时数（0-23）
- %I 12小时制小时数（01-12）
- %M 分钟数（00=59）
- %S 秒（00-59）
- %a 本地简化星期名称
- %A 本地完整星期名称
- %b 本地简化的月份名称
- %B 本地完整的月份名称
- %c 本地相应的日期表示和时间表示
- %j 年内的一天（001-366）
- %p 本地A.M.或P.M.的等价符
- %U 一年中的星期数（00-53）星期天为星期的开始
- %w 星期（0-6），星期天为星期的开始
- %W 一年中的星期数（00-53）星期一为星期的开始
- %x 本地相应的日期表示
- %X 本地相应的时间表示
- %Z 当前时区的名称
- %% %号本身

#实例
以下实例展示了 strptime() 函数的使用方法：

```
#!/usr/bin/python
import time

struct_time = time.strptime("30 Nov 00", "%d %b %y")
print "returned tuple: %s " % struct_time
```
以上实例输出结果为：

```
returned tuple: (2000, 11, 30, 0, 0, 0, 3, 335, -1)
```