越来越多的用户受加密勒索事件困扰。加密勒索软件利用系统漏洞，成功入侵用户业务服务器对全盘数据进行加密勒索，导致用户业务突然中断、数据泄露和数据丢失，带来严重业务风险。

本文分析了导致加密勒索病毒发生的不安全因素，并提供了相应防护方案，帮助您防护云服务器，远离加密勒索软件。

#不安全来源
通过对云上用户的调查分析，大部分用户未按照最佳的安全使用方式来使用云服务器资源，主要问题有：

- 关键账号存在弱口令或无认证机制。

	- 服务器关键账号（root、administrator）密码简单或无密码。
	- 数据库（Redis、MongoDB、MySQL、MSsql Server）等重要业务使用弱密码或无密码。


- 无访问控制策略，业务暴露在互联网上。RDP、SSH、Redis、MongoDB、MySQL、MSsql Server 等高危服务可以通过互联网直接访问。

- 服务器操作系统和软件存在高危漏洞。恶意攻击者可以利用服务器操作系统和应用服务软件存在的高危漏洞，上传加密勒索软件或执行勒索操作，实现远程攻击。

以上漏洞的利用成本较低，经常被黑客使用来发动数据库删除等勒索攻击，攻击者不需要获取账号密码就可以对业务造成重创。

#安全防护方案
为使云上用户尽量少受加密勒索软件影响，我们建议您参照并部署以下安全防护方案。

##数据备份与恢复
可靠的数据备份可以将勒索软件带来的损失最小化，但您也要对这些数据备份进行安全防护，避免数据感染和损坏。

- 建议您至少备份两份数据：本地备份和异地备份。
- 也建议您采用 多种不同的备份方式，以确保在发生勒索事件后，尽可能地挽回损失。

推荐您使用以下方法：

- ECS快照功能，具体操作请参考 ECS快照使用配置手册
- RDS提供的数据备份功能，具体操作请参考 RDS数据备份功能配置手册
- 使用OSS存储服务备份重要数据文件
- 由用户制定的数据备份策略或方案，如自建数据库MySQL备份

关键业务账号安全策略

- 阿里云主账号

阿里云为您分配的账号是所有云上业务的“关键钥匙”，一旦您所拥有的最高权限的“钥匙”泄露，黑客将从根本上掌握支撑云上业务的所有云服务资源，从而将直接威胁整体的云上业务安全。

阿里云为您提供账号登录多因素验证机制（MFA）、密码安全策略，和审计功能，您可以在控制台方便地启用和设置以上功能，确保云服务账号安全。

针对组织内部多角色场景，企业需要使用RAM服务为不同角色合理分配账号并授权，以防止在运维管理活动中，出现意外操作而带来安全风险。

- 业务最高权限账号

当您选用了云服务器，并在其中部署了关键业务（例如：数据库服务、文件服务、缓存等与数据强相关的核心重要服务），这些服务的最高管理员账号的安全是保证业务持续可靠运行的必要条件。

您需要妥善设置好账号和密码。

	- 不要将这些高危服务公开在互联网上，您可以参见 强化网络访问控制 部分配置强访问控制策略。
	- 启用认证鉴权功能。
	- 禁止使用root账号直接登录。
	- 如果您使用的是Windows系统，建议您修改 administrator 默认名称。
	- 为所有服务配置强密码。强密码要求至少8个字符以上，包含大小写字母、数字、特殊符号，不包含用户名、真实姓名或公司名称，不包含完整的单词。

推荐工具：阿里云访问控制RAM服务、系统和软件加固。

具体操作请参考 [RAM服务配置手册](https://help.aliyun.com/document_detail/28645.html?spm=5176.7748701.2.6.SDGkjw)。

##强化网络访问控制
精细化的网络管理是业务的第一道屏障。很多企业的网络安全架构缺少业务分区分段，一旦遭遇入侵，其影响面往往是全局的。在这种情况下，通过有效的安全区域划分、访问控制和准入机制可以防止或减缓渗透范围，阻止不必要的人员进入业务环境。

例如，您可以限制SSH、RDP等管理协议，并对FTP、Redis、MongoDB、Memcached、MySQL、MSSQL-Server、Oracle等数据相关服务的连接源IP进行访问控制，实现最小化访问范围，仅允许受信IP地址访问，并对出口网络行为实时分析和审计。

推荐您 使用安全的VPC网络。

- 通过VPC和安全组，划分不同安全等级的业务区域，让不同的业务处在不同的隔离空间。
- 配置入口/出口过滤安全组防火墙策略，同时在入口和出口进行过滤。例如，

	- 常用的数据库服务不需要在互联网直接管理或访问，可以通过配置入方向的访问控制策略防止数据库服务暴露在互联网上被黑客利用。
	- 也可以配置更严格的内网访问控制策略，例如：在内网入方向配置仅允许内网某IP访问内网的某台数据库服务器。

推荐工具：[VPC网络](https://www.aliyun.com/product/vpc?spm=5176.7748701.2.7.SDGkjw)、[安全组策略](https://help.aliyun.com/document_detail/25475.html?spm=5176.7748701.2.8.SDGkjw)

##搭建具有容灾能力的基础架构
高性能、具有冗余的基础架构能力是保障业务强固的基础条件。在云环境下，您可以使用SLB集群搭建高可用架构。当某一个节点发生紧急问题，高可用架构可以无缝切换至备用节点，既防止业务中断，也防止数据丢失。

在资源允许的条件下，企业或组织可以搭建同城或异地容灾备份系统，当主系统出现发生勒索事件后，可以快速切换到备份系统，从而保证业务的连续性。

推荐工具：阿里云SLB、阿里云RDS等高性能服务组合而成的容灾架构

##定期进行外部端口扫描
端口扫描可以用来检验企业的弱点暴露情况。如果企业有一些服务连接到互联网，需要确定哪些业务是必须要发布到互联网上，哪些仅需要内部访问。公开到互联网的服务数量越少，攻击者的攻击范围就越窄，从而遭受的安全风险就越小。

推荐工具：[阿里云云盾安全管家服务](https://www.aliyun.com/product/sos?spm=5176.7748701.2.9.SDGkjw)

##定期进行安全测试
企业IT管理人员需要定期对业务软件资产进行安全漏洞探测，一旦确定有公开暴露的服务，应使用漏洞扫描工具对其进行扫描，尽快修复扫描发现的漏洞。同时，日常也应该不定期关注软件厂商发布的安全漏洞信息和补丁信息，及时做好漏洞修复管理工作。

推荐工具：[VPC网络](https://www.aliyun.com/product/vpc?spm=5176.7748701.2.10.SDGkjw)、[安全组](https://help.aliyun.com/document_detail/25475.html?spm=5176.7748701.2.11.SDGkjw)、[阿里云云盾安全管家服务](https://www.aliyun.com/product/sos?spm=5176.7748701.2.12.SDGkjw)、主机系统和服务软件安全加固

##基础安全运维
- 制定并实施IT软件安全配置，对操作系统（Windows、Linux）和软件（FTP、Apache、Nginx、Tomcat、Mysql、MS-Sql Server、Redis、MongdoDB、Mecached等服务）初始化安全加固，并定期核查其有效性。
- 为Windows操作系统云服务器安装防病毒软件，并定期更新病毒库。
- 定期更新补丁。
- 修改 administrator 默认名称，为登录账号配置强口令。
- 开启日志记录功能，集中管理日志和审计分析。
- 合理地分配账号、授权，并开启审计功能，例如：为服务器、RDS数据库建立不同权限账号并启用审计功能；如果有条件，可以实施类似堡垒机、VPN等更严格的访问策略。
- 实施强密码策略，并定期更新维护，对于所有操作行为严格记录并审计。
- 对所有业务关键点进行实时监控，当发现异常时，立即介入处理。

推荐工具：[阿里云云盾安骑士](https://www.aliyun.com/product/aegis?spm=5176.7748701.2.13.SDGkjw)

##应用系统代码安全
大部分安全问题来自程序代码不严谨，代码安全直接影响到业务风险。根据经验，代码层的安全需要程序员从一开始就将安全架构设计纳入到整体软件工程内，按照标准的软件开发流程，在每个环节内关联安全因素。

对于一般企业，需要重点关注开发人员或软件服务提供上的安全编码和安全测试结果，尤其是对开发完成的业务代码进行代码审计评估和上线后的黑盒测试（也可以不定期地进行黑盒渗透测试）。

推荐工具：[阿里云云盾先知计划](https://www.aliyun.com/product/xianzhi?spm=5176.7748701.2.14.SDGkjw)、[阿里云云盾web应用防火墙(WAF)](https://www.aliyun.com/product/waf?spm=5176.7748701.2.15.SDGkjw)、SDL标准流程

##建立全局的外部威胁和情报感知能力
安全是动态对抗的过程，在安全事件发生之前，就要时刻了解和识别外部不同类型的风险。做安全的思路应该从防止安全入侵这种不可能的任务转到了防止损失这一系列关键任务上。防范措施必不可少，但是基于预警、响应的时间差也同样关键。而实现这种快速精准的预警能力需要对外面的信息了如指掌，所以建立有效的监控和感知体系是实现安全管控措施是不可少的环节，更是安全防护体系策略落地的基础条件。

您可以登录阿里云控制台，到云盾菜单中免费开通阿里云态势感知服务，查看实时的外部攻击行为和内部漏洞（弱点）情况。

推荐工具：[阿里云云盾态势感知](https://www.aliyun.com/product/sas?spm=5176.7748701.2.16.SDGkjw)、大数据安全分析平台

##建立安全事件应急响应流程和预案
在安全攻防的动态过程中，建议您为突发的安全事件准备好应急策略。在安全事件发生后，要通过组织快速响应、标准化的应急响应流程、规范的事件处置规范来降低安全事件带来的损失。

推荐工具：可管理的安全服务（MSS）、安全事件应急响应服务

#更多参考
请参考以下相关加固文档：

[Windows操作系统加固手册](https://help.aliyun.com/knowledge_detail/49781.html?spm=5176.7748701.2.17.SDGkjw)
[Linux操作系统加固手册](https://help.aliyun.com/knowledge_detail/49809.html?spm=5176.7748701.2.18.SDGkjw)
[FTP服务加固手册](https://help.aliyun.com/knowledge_detail/37452.html?spm=5176.7748701.2.19.SDGkjw)
[MySQL服务加固手册](https://help.aliyun.com/knowledge_detail/49568.html?spm=5176.7748701.2.20.SDGkjw)
[Redis服务加固手册](https://help.aliyun.com/knowledge_detail/37447.html?spm=5176.7748701.2.21.SDGkjw)
[MongoDB服务加固手册](https://help.aliyun.com/knowledge_detail/37451.html?spm=5176.7748701.2.22.SDGkjw)
[Memcached服务加固手册](https://help.aliyun.com/knowledge_detail/37553.html?spm=5176.7748701.2.23.SDGkjw)