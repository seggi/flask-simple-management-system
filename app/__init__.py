from flask import Flask, render_template  
from flask_mail import Mail 
from flask_moment import Moment 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_marshmallow import Marshmallow
from flaskext.mysql import MySQL
from config import config


mail = Mail()
moment = Moment()
db = SQLAlchemy()
# ma = Marshmallow()
mysqldb = MySQL()




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    # ma.init_app(app)
    mysqldb.init_app(app)
    # ui.init_app(app)

    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'

    login_manager.init_app(app)
    # mysqldb.init_app(app)

    from .models import NkRegister

    @login_manager.user_loader
    def load_user(user_id):
        return NkRegister.query.get(int(user_id))



    from . main import main as main_blueprint
    from . auth import auth as auth_blueprint 

    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint, url_prefix='/main')

    return app




# ????????????????????????????????????????????????????????????????????????
# def create_app():
#     app = Flask(__name__)

#     from . main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     return app












# def create_app():
#     app = Flask(__name__)

#     db.init_app(app)
#     # ma.init_app(app)

#     login_manager = LoginManager()
#     login_manager.session_protection = 'strong'
#     login_manager.login_view = 'auth.login'

#     login_manager.init_app(app)
#     # mysqldb.init_app(app)


#     from .models import NkRegister

#     @login_manager.user_loader
#     def load_user(user_id):
#         return NkRegister.query.get(int(user_id))

#     from . main import main as main_blueprint
#     from . auth import auth as auth_blueprint 

#     app.register_blueprint(auth_blueprint)
#     app.register_blueprint(main_blueprint,  url_prefix="/main")
    

#     return app