from flask import redirect, flash, url_for
from flask_admin import AdminIndexView, expose
from flask_login import login_required, current_user


class DashboardView(AdminIndexView):
    @expose('/', methods=['GET'])
    @login_required
    def index(self):
        if current_user.is_authenticated and current_user.role == 'admin':
            return self.render('admin/index.html')
        else:
            flash('У вас нет прав доступа к панели администратора')
            return redirect(url_for('homepage'))