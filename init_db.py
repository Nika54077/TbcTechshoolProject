from ext import app, db
from models import User


with app.app_context():
    db.create_all()

    admin_user = User("admin_user", "adminpassword5432", "admin")
    db.session.add(admin_user)
    db.session.commit()
