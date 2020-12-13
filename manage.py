import os 
from flaskwebgui import FlaskUI 
from flask_script import Manager, Shell 
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import (NkRegister, NkPhysicalProduct, NkVirtualProduct,
    NkCurrencyType, NkLaguageContent, NkLaguage, NkExpenses, NkEmployee, 
    NkSellPhysicalProduct, NkSellVirtualProduct, NkRepport)



app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager =  Manager(app)
migrate = Migrate(app, db)
ui = FlaskUI(app)


def make_shell_content():
    return dict(app=app, db=db, user=NkRegister, physicalpr=NkPhysicalProduct, virtualpr=NkVirtualProduct,
        nkcurrency=NkCurrencyType,  NkLaguage=NkLaguage, NkExpenses=NkExpenses, NkEmployee=NkEmployee, 
    NkSellPhysicalProduct=NkSellPhysicalProduct, NkSellVirtualProduct=NkSellVirtualProduct,
     NkRepport=NkRepport)

manager.add_command("shell", Shell(make_context=make_shell_content))
manager.add_command('db', MigrateCommand)

if __name__=='__main__':
    manager.run()


# --------------------------------------------------------------------------
# python3 manage.py db migrate -m "initial migration"


   

# app = create_app()
# ui = FlaskUI(app)

# manager = Manager(ui)
# migrate = Migrate(app, db)

# def make_shell_content():
#     return dict(app=app, db=db, user=NkRegister, physicalpr=NkPhysicalProduct, virtualpr=NkVirtualProduct)

# manager.add_command("shell", Shell(make_context=make_shell_content))
# manager.add_command('db', MigrateCommand)

# if __name__=='__main__':
#     app.run()

