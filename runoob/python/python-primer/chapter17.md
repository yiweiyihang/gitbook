# Python 列表(List)

序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

```
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
```

与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
访问列表中的值
使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：


```
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
```

以上实例输出结果：

```
list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]
```

# 更新列表
你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示：


```
#!/usr/bin/python

list = ['physics', 'chemistry', 1997, 2000];

print "Value available at index 2 : "
print list[2];
list[2] = 2001;
print "New value available at index 2 : "
print list[2];
```

注意：我们会在接下来的章节讨论append()方法的使用
以上实例输出结果：

```
Value available at index 2 :
1997
New value available at index 2 :
2001
```

# 删除列表元素
可以使用 del 语句来删除列表的的元素，如下实例：

```
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000];

print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;
```

以上实例输出结果：


```
['physics', 'chemistry', 1997, 2000]
After deleting value at index 2 :
['physics', 'chemistry', 2000]
```

注意：我们会在接下来的章节讨论remove()方法的使用

# Python列表脚本操作符

列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
如下所示：

|Python 表达式	|结果	|描述
|-|-|-|
|len([1, 2, 3])	|3	|长度
|[1, 2, 3] + [4, 5, 6]	|[1, 2, 3, 4, 5, 6]	|组合
|['Hi!'] * 4	|['Hi!', 'Hi!', 'Hi!', 'Hi!']	|重复
|3 in [1, 2, 3]	|True	|元素是否存在于列表中
|for x in [1, 2, 3]: print x,	|1 2 3	|迭代


# Python列表截取

Python的列表截取与字符串操作类型，如下所示：

```
L = ['spam', 'Spam', 'SPAM!']
```

操作：

|Python 表达式	|结果	|描述
|L[2]	|'SPAM!'	|读取列表中第三个元素
|L[-2]	|'Spam'	|读取列表中倒数第二个元素
|L[1:]	|['Spam', 'SPAM!']	|从第二个元素开始截取列表


# Python列表函数&方法

Python包含以下函数:

|序号	|函数|描述
|-|-|-|
|1	|[cmp(list1, list2)](./att/cmp.md)|比较两个列表的元素
|2	|[len(list)](./att/len.md)|列表元素个数
|3	|[max(list)](./att/list.max.md)|返回列表元素最大值
|4	|[min(list)](./att/list.min.md)|返回列表元素最小值
|5	|[list(seq)](./att/list.md)|将元组转换为列表

Python包含以下方法:

|序号	|方法|描述
|-|-|-|
|1	|[list.append(obj)](./att/append.md)|在列表末尾添加新的对象
|2	|[list.count(obj)](./att/list.count.md)|统计某个元素在列表中出现的次数
|3	|[list.extend(seq)](./att/extend.md)|在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
|4	|[list.index(obj)](./att/list.index.md)|从列表中找出某个值第一个匹配项的索引位置
|5	|[list.insert(index, obj)](./att/insert.md)|将对象插入列表
|6	|[list.pop(obj=list[-1])](./att/pop.md)|移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
|7	|[list.remove(obj)](./att/remove.md)|移除列表中某个值的第一个匹配项
|8	|[list.reverse()](./att/reverse.md)|反向列表中元素
|9	|[list.sort([func]](./att/sort.md))|对原列表进行排序