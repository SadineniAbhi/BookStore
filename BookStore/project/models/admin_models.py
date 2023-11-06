from flask_admin.contrib.sqla import ModelView
from flask_admin import expose
from flask_admin import Admin,AdminIndexView
from flask_login import current_user
class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.isadmin

class NewAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('custom_index.html')
    
    def is_accessible(self):
        self._template_args['custom_title'] = 'Custom Admin Page'
        return current_user.isadmin