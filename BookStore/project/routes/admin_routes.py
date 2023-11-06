from flask_admin import Admin
from project.models.admin_models import AdminIndexView, AdminModelView, NewAdminIndexView
from project import app, db
from project.models.order_models import Order, OrderItem
from project.models.Book_model import Book
from project.models.user_model import User

admin = Admin(app,index_view=NewAdminIndexView())
admin.add_view(AdminModelView(OrderItem,db.session))
admin.add_view(AdminModelView(User,db.session))
admin.add_view(AdminModelView(Book,db.session))