#6-2-1 更新DOM

拿到一个DOM节点后，我们可以对它进行更新。

可以直接修改节点的文本，方法有两种：

一种是修改innerHTML属性，这个方式非常强大，不但可以修改一个DOM节点的文本内容，还可以直接通过HTML片段修改DOM节点内部的子树：

	// 获取<p id="p-id">...</p>
	var p = document.getElementById('p-id');
	// 设置文本为abc:
	p.innerHTML = 'ABC'; // <p id="p-id">ABC</p>
	// 设置HTML:
	p.innerHTML = 'ABC <span style="color:red">RED</span> XYZ';
	// <p>...</p>的内部结构已修改
用innerHTML时要注意，是否需要写入HTML。如果写入的字符串是通过网络拿到了，要注意对字符编码来避免XSS攻击。

第二种是修改innerText或textContent属性，这样可以自动对字符串进行HTML编码，保证无法设置任何HTML标签：
	
	// 获取<p id="p-id">...</p>
	var p = document.getElementById('p-id');
	// 设置文本:
	p.innerText = '<script>alert("Hi")</script>';
	// HTML被自动编码，无法设置一个<script>节点:
	// <p id="p-id">&lt;script&gt;alert("Hi")&lt;/script&gt;</p>
两者的区别在于读取属性时，innerText不返回隐藏元素的文本，而textContent返回所有文本。另外注意IE<9不支持textContent。

修改CSS也是经常需要的操作。DOM节点的style属性对应所有的CSS，可以直接获取或设置。因为CSS允许font-size这样的名称，但它并非JavaScript有效的属性名，所以需要在JavaScript中改写为驼峰式命名fontSize：

	// 获取<p id="p-id">...</p>
	var p = document.getElementById('p-id');
	// 设置CSS:
	p.style.color = '#ff0000';
	p.style.fontSize = '20px';
	p.style.paddingTop = '2em';
##练习

有如下的HTML结构：

javascript

Java

	<!-- HTML结构 -->
	<div id="test-div">
	  <p id="test-js">javascript</p>
	  <p>Java</p>
	</div>
请尝试获取指定节点并修改：

	'use strict';
	
	// 获取<p>javascript</p>节点:
	var js = ???;
	
	// 修改文本为JavaScript:
	// TODO:
	
	// 修改CSS为: color: #ff0000, font-weight: bold
	// TODO:
	
	// 测试:
	if (js && js.parentNode && js.parentNode.id === 'test-div' && js.id === 'test-js') {
	    if (js.innerText === 'JavaScript') {
	        if (js.style && js.style.fontWeight === 'bold' && (js.style.color === 'red' || js.style.color === '#ff0000' || js.style.color === '#f00' || js.style.color === 'rgb(255, 0, 0)')) {
	            alert('测试通过!');
	        } else {
	            alert('CSS样式测试失败!');
	        }
	    } else {
	        alert('文本测试失败!');
	    }
	} else {
	    alert('节点测试失败!');
	}