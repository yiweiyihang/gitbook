# 网站备份文件泄露

## 漏洞描述
网站备份文件泄露指管理员误将网站备份文件或是敏感信息文件存放在某个网站目录下。

外部黑客可通过暴力破解文件名等方法下载该备份文件，导致网站敏感信息泄露。

## 修复建议
- 不要在网站目录下存放网站备份文件或包含敏感信息的文件。

- 如需存放该类文件，请将文件名命名为难以破解的字符串。