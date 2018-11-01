# 挂马攻击和防御
   
## 什么是挂马攻击
挂马攻击指，攻击者在已经获得控制权的网站的网页中嵌入恶意代码（一般通过 IFrame、Script 引用）。

当用户访问该网页时，嵌入的恶意代码利用浏览器本身的漏洞、第三方 ActiveX 漏洞，或者其它插件（如 Flash、PDF 插件等）漏洞，在用户不知情的情况下下载并执行恶意木马。

## 挂马攻击有什么危害
网站被挂马后，表示该站点已经被黑客成功入侵。黑客可以获取用户账号密码、业务数据等其他敏感数据。

## 如何防御挂马攻击
- 使用云盾 先知 在业务代码上线前，进行代码安全测试、白盒代码审计等。

- 日常运维过程中，定期检测并修补网站本身以及网站所在服务端环境的各类漏洞，及时更新操作系统、应用服务软件补丁等。

- 使用云盾 Web 应用防火墙（WAF）进行安全防护。