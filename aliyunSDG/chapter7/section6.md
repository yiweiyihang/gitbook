# 域名未设置 SPF 解析记录

## 漏洞描述
SPF 记录是一种域名服务（DNS）记录，用于标识哪些邮件服务器可以代表您的域名发送电子邮件。 SPF 记录的目的是为了防止垃圾邮件发送者在您的域名上，使用伪造的发件人地址发送邮件。

若您未对您的域名添加 SPF 解析记录，则黑客可以仿冒以该域名为后缀的邮箱，来发送垃圾邮件。

## 修复方案
在您的 DNS 服务提供商处，为您的域名添加一条 TXT 记录：

- 将主机字段（Host）设置为您子域名的名称。（例如，如果您的电子邮件地址是contact@mail.example.com，则为 mail。）如果不使用子域名，则将其设为@。

- 用您的 SPF 记录填写 TXT 值字段。例如 v = spf1 a mx include：secureserver.net〜all。