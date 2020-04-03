
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from db import UserModel, RevokedAccessTokenModel, RevokedRefreshTokenModel

from main import flask_app as app, db


#app.config.from_object(os.environ['APP_SETTINGS'])
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

# ... some more code here ...

if __name__ == "__main__":
    manager.run()
    db.create_all()
