##环境
###什么是一个环境?
Rancher 支持将资源分组归属到多个环境。每个环境具有自己独立的基础设施资源及服务，并由一个或多个用户、团队或组织管理。例如，你可以创建独立的“开发”、“测试”及“生产”环境以确保环境之间的安全隔离，将“开发”环境的访问权限赋予全部人员，但限制“生产”环境的访问权限给一个小的团队。

所有主机和Rahcner资源, 比如容器, 基础设施服务等, 都在环境中被创建, 并且属于一个环境。

###添加环境
要添加一个环境，把鼠标移动到位于左上角的当前环境， 此时会出现一个带有所有可用的环境下拉框，以及一个 环境管理 连接。点击 环境管理。

导航到 环境 页面后，你会看到一个环境列表和一个环境模板列表。如果你是 Rancher 的
管理员用户，你会看到一个所有环境的列表，即使你不是该环境的成员。任何环境模板都对所有用户可见。

点击 添加环境。每个环境都有自己的名字和描述，你可以选择你要使用的环境模板。在环境模板中，你可以看到哪个基础设施服务是启用的。

> 注意：
如果没有配置 访问控制， 所有环境都可以被其它 Rancher 的用户访问到。 环境没有任何所属关系。

有两种方法可以将成员添加到一个环境里:

- 输入用户名，点击 + 把用户添加到成员列表中。如果该用户名不在列表中，则不会被加入到环境中。
- 在某些认证方式下，右侧有一个 + 下拉框按钮，这个下拉框会出现组织/团队，你可以将用户或团队加入到环境里。

你可以把每个成员(既个人、团队、或组织)的角色设置为所有者、成员、受限制的成员或只读用户中的一个。默认情况下，新添加的用户角色为成员。通过用户名旁边的下拉框，可以改变相应用户的角色. 对于环境所有者，你可以随时编辑成员列表以及成员角色。 只有环境的所有者能编辑环境的成员以及其角色。

注意：
只有所有者和管理员才能查看环境的基础设施服务。

点击 创建 会创建一个环境，所有在成员列表中的用户都立即可以看到这个环境。创建完环境并且添加主机后，Rancher会开始自动部署已启用的基础设施服务。

###停用和删除环境
创建环境后，所有者可能想停用或删除该环境。

环境被停用后，这个环境不再对环境成员可见，但环境的所有者还可以看到并启用这个环境。在环境停用后你不能变更环境的成员，直到该环境被再次启用。环境被停用后所有资源不能再变更，如果你要变更你的基础设施服务，你需要在环境停用之前变更。

要删除一个环境，先要停用这个环境。环境删除后，这个环境所有的镜像仓库，负载均衡，API keys 都会从 Rancher 移除。所有通过 Rancher UI 创建，用 Docker Machine 启用的主机也会在云提供商中被用 Docker Machine 移除。如果你已经通过自定义的方式添加了一台主机，那么这台主机在云提供商中不会被移除。

###成员编辑
只有环境的所有者可以编辑环境的成员。在环境管理页面，你可以点击编辑进入环境成员编辑页面， 在编辑页面，你可以通过下拉框添加环境成员。

如果要删除环境成员，可以点击成员列表旁边的X。注意，单个成员被删除时，如果被删除的成员所属的团队或组织是这个环境的成员，那么他们仍然可以访问这个环境，

所有者可以更改任何环境成员的角色，你只需要选择成员的相应角色。

###成员角色
####所有者
所有者有在环境中添加和删除用户的权限，也可以修改环境的状态。在环境的成员列表中，所有者还可以改变环境成员的角色。

因为无法编辑环境模版，所有者可以通过应用商店来修改环境的基础设施服务。环境模版只能在创建环境时使用。

####成员
一个环境的成员可以在Rancher里面做任何不影响环境本身的操作。成员不能添加／移除其他成员，不能改变其他已存在成员的角色，也不能查看任何基础设施服务。

####受限
环境的受限成员只能够做与应用和服务相关的操作。受限成员能对所有服务的容器做任何操作，即，启动、停止、删除、升级、克隆和编辑。从应用、 服务和容器操作的角度来说，受限成员是不受限制的。

对受限成员的限制体现在他们对主机的操作上。受限成员只能查看一个环境的主机，而不能添加，编辑，移除环境的主机。

> 注意：
受限成员不能添加、移除主机标签，只有成员和所有者才能改变主机的标签。

####只读
只读成员只能查看环境的资源。 他们可以查看 主机、应用、服务和容器。但只读成员不能对它们作任何创建、编辑和移除操作。

> 注意：
只读成员可以查看容器的日志。

为了使非所有者可以设置环境的成员，你可以通过更新API配置project.set.member.roles来实现这一点。

###什么是环境模版
环境模版可以让用户定义需要部署的基础设施服务组合。基础设施服务包括（但不限于）容器编排 (即Cattle，Kubernetes、Mesos、Swarm)、网络、Rancher 服务 (即 健康检查、DNS、Metadata、调度、服务发现、存储。

容器的编排方式很多，Rancher提供了一套默认的模版以及推荐使用的基础设施服务用于容器编排。其中的一些基础设施服务（Rancher调度器只能在Cattle环境下使用 ），其他的编排引擎也依赖他们，因为这些服务被用来启动其它基础设施服务。除了默认的模版，你也可以创建自己的模版。通过自己创建模版，你可以选者环境中任何你想要的基础设施服务组合。只有所有者或管理员可以查看和编辑环境的基础设施服务。

在和其它用户共享环境前， 我们推荐先设置好访问控制。用户被加入一个环境后, 他们就拥有了创建服务和管理资源的权限。

> 注意：
基础设施资源不可跨环境共享。镜像仓库、证书 和环境API密钥也不能跨环境。

###添加环境模版
要添加一个新环境，你可以把鼠标移动到左上角的环境下拉框。下拉框中会出现所有可用的环境以及环境管理的链接。 点击环境管理

在环境页面后，你可以看到一个环境列表和一个环境模版列表。 点击添加模版

为模版选择一个 名称 和 描述， 选择分享自己模版的方式。 模版可以是私有（只有自己可见）和公有（管理员可见）。

基础设施服务包括，但不限于容器编排、存储和网络。默认的基础设施服务会自动启动。

###编辑 & 删除环境模版
创建环境模版后，你可以在模版中编辑启用哪个基础设施服务。虽然环境模版是可以编辑的，但已经存在的基于模版创建的环境不会随模版自动更新。

你可以在任何时候删除一个环境模版，因为它们只有在启动环境的时候才会被用到（用来指定哪些基础设施服务会被启用）。环境与环境模版没有直接绑定关系，所以删除环境模版不会影响环境。

###权限键:
- C = 创建
- R = 读取 (查看)
- U = 更新
- D = 删除

成员关联的权限

| -|所有者	|成员	|受限	|只读
|:-|:-|:-|:-|:-|
|环境成员	|RUD	|R	|R	|R
|主机	|CRUD	|CRUD	|R	|R
|容器	|CRUD	|CRUD	|CRUD	|R
|存储	|CRUD	|CRUD	|CRUD	|R
|密文	|CRUD	|CRUD	|CRUD	|R
|证书	|CRUD	|CRUD	|CRUD	|R
|镜像仓库	|CRUD	|CRUD	|CRUD	|R
|Webhooks	|CRD	|CRD	|CRD	|R
|用户应用	|CRUD	|CRUD	|CRUD	|R
|基础设施应用	|CRUD	|RUD	|R	|R

| -|所有者	|成员	|受限	|只读
|:-|:-|:-|:-|:-|
|用户容器	|start, stop, delete, restart, exec	|start, stop, delete, restart, exec	|start, stop, delete, restart, exec|-|	 
|基础设施容器	|start, stop, delete, restart, exec	|start, stop, delete, restart, exec|-|-|	 	 

> 注意：
了解更多基础设施服务。用户应用，容器和服务没有被定义在基础设施服务中。

账户类型关联的权限

|-	|管理员	|用户|
|:-|:-|:-|
|私有模版	|CRUD	|CRUD
|共有模版	|CRUD	|R
|环境	|CRUD	|CRUD