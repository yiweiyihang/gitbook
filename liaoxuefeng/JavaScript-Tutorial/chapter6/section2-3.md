#6-2-3 删除DOM


删除一个DOM节点就比插入要容易得多。

要删除一个节点，首先要获得该节点本身以及它的父节点，然后，调用父节点的removeChild把自己删掉：

	// 拿到待删除节点:
	var self = document.getElementById('to-be-removed');
	// 拿到父节点:
	var parent = self.parentElement;
	// 删除:
	var removed = parent.removeChild(self);
	removed === self; // true
注意到删除后的节点虽然不在文档树中了，但其实它还在内存中，可以随时再次被添加到别的位置。

当你遍历一个父节点的子节点并进行删除操作时，要注意，children属性是一个只读属性，并且它在子节点变化时会实时更新。

例如，对于如下HTML结构：

	<div id="parent">
	    <p>First</p>
	    <p>Second</p>
	</div>
当我们用如下代码删除子节点时：

	var parent = document.getElementById('parent');
	parent.removeChild(parent.children[0]);
	parent.removeChild(parent.children[1]); // <-- 浏览器报错
浏览器报错：parent.children[1]不是一个有效的节点。原因就在于，当<p>First</p>节点被删除后，parent.children的节点数量已经从2变为了1，索引[1]已经不存在了。

因此，删除多个节点时，要注意children属性时刻都在变化。

##练习

- JavaScript
- Swift
- HTML
- ANSI C
- CSS
- DirectX


	<!-- HTML结构 -->
	<ul id="test-list">
	    <li>JavaScript</li>
	    <li>Swift</li>
	    <li>HTML</li>
	    <li>ANSI C</li>
	    <li>CSS</li>
	    <li>DirectX</li>
	</ul>

把与Web开发技术不相关的节点删掉：


	'use strict';
	
	// TODO
	
	// 测试:
	;(function () {
	    var
	        arr, i,
	        t = document.getElementById('test-list');
	    if (t && t.children && t.children.length === 3) {
	        arr = [];
	        for (i = 0; i < t.children.length; i ++) {
	            arr.push(t.children[i].innerText);
	        }
	        if (arr.toString() === ['JavaScript', 'HTML', 'CSS'].toString()) {
	            alert('测试通过!');
	        }
	        else {
	            alert('测试失败: ' + arr.toString());
	        }
	    }
	    else {
	        alert('测试失败!');
	    }
	})();