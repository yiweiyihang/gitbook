#23-6 Day 6 - 添加配置文件


有了Web框架和ORM框架，我们就可以开始装配App了。

通常，一个Web App在运行时都需要读取配置文件，比如数据库的用户名、口令等，在不同的环境中运行时，Web App可以通过读取不同的配置文件来获得正确的配置。

由于Python本身语法简单，完全可以直接用Python源代码来实现配置，而不需要再解析一个单独的.properties或者.yaml等配置文件。

默认的配置文件应该完全符合本地开发环境，这样，无需任何设置，就可以立刻启动服务器。

我们把默认的配置文件命名为config_default.py：

	# config_default.py
	
	configs = {
	    'db': {
	        'host': '127.0.0.1',
	        'port': 3306,
	        'user': 'www-data',
	        'password': 'www-data',
	        'database': 'awesome'
	    },
	    'session': {
	        'secret': 'AwEsOmE'
	    }
	}
上述配置文件简单明了。但是，如果要部署到服务器时，通常需要修改数据库的host等信息，直接修改config_default.py不是一个好办法，更好的方法是编写一个config_override.py，用来覆盖某些默认设置：

	# config_override.py
	
	configs = {
	    'db': {
	        'host': '192.168.0.100'
	    }
	}
把config_default.py作为开发环境的标准配置，把config_override.py作为生产环境的标准配置，我们就可以既方便地在本地开发，又可以随时把应用部署到服务器上。

应用程序读取配置文件需要优先从config_override.py读取。为了简化读取配置文件，可以把所有配置读取到统一的config.py中：

	# config.py
	configs = config_default.configs
	
	try:
	    import config_override
	    configs = merge(configs, config_override.configs)
	except ImportError:
	    pass
这样，我们就完成了App的配置。