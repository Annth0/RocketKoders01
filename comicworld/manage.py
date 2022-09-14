from flask_script import Manager
from app import initializar_app

app = initializar_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
    
    #python manage.py runserver