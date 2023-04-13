from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app.models.Bread import Bread
from app.models.Purchase import Purchase
from app.models.User import User


class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.email == "test@test.com"


admin = Admin(app)
admin.add_view(CustomModelView(Bread, db.session))
admin.add_view(CustomModelView(Purchase, db.session))
admin.add_view(CustomModelView(User, db.session))
