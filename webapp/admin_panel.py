from flask_admin import AdminIndexView, expose


class DashboardView(AdminIndexView):
	@expose('/')
	def index_admin(self):
		return self.render('admin/index.html')
