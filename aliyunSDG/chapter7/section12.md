# 越权漏洞

## 漏洞描述
越权漏洞指在网站中某个页面上，能看到不属于当前用户身份的信息，如以用户 A 的身份能看到用户 B 的信息。

## 修复方案
- 如果您使用的是第三方 CMS，建议您将 CMS 升级到官方最新版本。

- 如果您使用自己编写的网站程序，建议您限制该页面可访问的对象，如添加权限认证、或指定 IP 才能访问。

- 如果该页面不需要使用，建议您把页面删除。