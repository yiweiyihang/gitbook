#15-7 XML


XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。

##DOM vs SAX

操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

正常情况下，优先考虑SAX，因为DOM实在太占内存。

在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

举个例子，当SAX解析器读到一个节点时：

	<a href="/">python</a>
会产生3个事件：

1. start_element事件，在读取`<a href="/">`时；

2. char_data事件，在读取python时；

3. end_element事件，在读取</a>时。

用代码实验一下：

	from xml.parsers.expat import ParserCreate
	
	class DefaultSaxHandler(object):
	    def start_element(self, name, attrs):
	        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
	
	    def end_element(self, name):
	        print('sax:end_element: %s' % name)
	
	    def char_data(self, text):
	        print('sax:char_data: %s' % text)
	
	xml = r'''<?xml version="1.0"?>
	<ol>
	    <li><a href="/python">Python</a></li>
	    <li><a href="/ruby">Ruby</a></li>
	</ol>
	'''
	
	handler = DefaultSaxHandler()
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.EndElementHandler = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	parser.Parse(xml)
需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。

除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：

	L = []
	L.append(r'<?xml version="1.0"?>')
	L.append(r'<root>')
	L.append(encode('some & data'))
	L.append(r'</root>')
	return ''.join(L)
如果要生成复杂的XML呢？建议你不要用XML，改成JSON。

##小结

解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。

##练习

请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取当天和第二天的天气：

http://weather.yahooapis.com/forecastrss?u=c&w=2151330

参数w是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。

	# -*- coding:utf-8 -*-
	
	from xml.parsers.expat import ParserCreate
	
	class WeatherSaxHandler(object):
	    pass
	
	def parse_weather(xml):
	    return {
	        'city': 'Beijing',
	        'country': 'China',
	        'today': {
	            'text': 'Partly Cloudy',
	            'low': 20,
	            'high': 33
	        },
	        'tomorrow': {
	            'text': 'Sunny',
	            'low': 21,
	            'high': 34
	        }
	    }
	
	# 测试:
	data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
	<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
	    <channel>
	        <title>Yahoo! Weather - Beijing, CN</title>
	        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
	        <yweather:location city="Beijing" region="" country="China"/>
	        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
	        <yweather:wind chill="28" direction="180" speed="14.48" />
	        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
	        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
	        <item>
	            <geo:lat>39.91</geo:lat>
	            <geo:long>116.39</geo:long>
	            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
	            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
	            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
	            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
	            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
	            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
	            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
	        </item>
	    </channel>
	</rss>
	'''
	weather = parse_weather(data)
	assert weather['city'] == 'Beijing', weather['city']
	assert weather['country'] == 'China', weather['country']
	assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
	assert weather['today']['low'] == 20, weather['today']['low']
	assert weather['today']['high'] == 33, weather['today']['high']
	assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
	assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
	assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
	print('Weather:', str(weather))


##参考源码

- 本地

[use_sax.py](../code/chapter15/15-7-use_sax.py)


- github

[use_sax.py](https://github.com/michaelliao/learn-python3/blob/master/samples/commonlib/use_sax.py)