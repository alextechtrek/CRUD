from flask import Flask
from orm.setting import db
from flask_migrate import Migrate
from views.products import products_bp

# create the app
app = Flask(__name__)
app.register_blueprint(products_bp)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
Migrate(app, db)


if __name__ == "__main__":
    app.run(port=3456, debug=True)
