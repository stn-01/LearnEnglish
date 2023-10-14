from flask import redirect, flash, url_for
from flask_admin import AdminIndexView, expose
from flask_login import login_required, current_user
from flask_admin.contrib.sqla import ModelView


class DashboardView(AdminIndexView):
    @expose('/', methods=['GET'])
    @login_required
    def index(self):
        index_template = 'admin/index.html'
        if current_user.is_authenticated and current_user.role == 'admin':
            return self.render(index_template)
        else:
            flash('У вас нет прав доступа к панели администратора')
            return redirect(url_for('homepage'))


class UserView(ModelView):
    column_list = ('id', 'name', 'nickname', 'email', 'role')
