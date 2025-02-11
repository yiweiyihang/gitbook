#24-14 Day 14 - 完成Web App


在Web App框架和基本流程跑通后，剩下的工作全部是体力活了：在Debug开发模式下完成后端所有API、前端所有页面。我们需要做的事情包括：

把当前用户绑定到request上，并对URL/manage/进行拦截，检查当前用户是否是管理员身份：

	@asyncio.coroutine
	def auth_factory(app, handler):
	    @asyncio.coroutine
	    def auth(request):
	        logging.info('check user: %s %s' % (request.method, request.path))
	        request.__user__ = None
	        cookie_str = request.cookies.get(COOKIE_NAME)
	        if cookie_str:
	            user = yield from cookie2user(cookie_str)
	            if user:
	                logging.info('set current user: %s' % user.email)
	                request.__user__ = user
	        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
	            return web.HTTPFound('/signin')
	        return (yield from handler(request))
	    return auth

后端API包括：

- 获取日志：GET /api/blogs

- 创建日志：POST /api/blogs

- 修改日志：POST /api/blogs/:blog_id

- 删除日志：POST /api/blogs/:blog_id/delete

- 获取评论：GET /api/comments

- 创建评论：POST /api/blogs/:blog_id/comments

- 删除评论：POST /api/comments/:comment_id/delete

- 创建新用户：POST /api/users

- 获取用户：GET /api/users

管理页面包括：

- 评论列表页：GET /manage/comments

- 日志列表页：GET /manage/blogs

- 创建日志页：GET /manage/blogs/create

- 修改日志页：GET /manage/blogs/

- 用户列表页：GET /manage/users

用户浏览页面包括：

- 注册页：GET /register

- 登录页：GET /signin

- 注销页：GET /signout

- 首页：GET /

- 日志详情页：GET /blog/:blog_id

把所有的功能实现，我们第一个Web App就宣告完成！

##参考源码

[day-14](https://github.com/michaelliao/awesome-python3-webapp/tree/day-14)