from flask_script import Manager, Server
from appdraft import inicializar_app
from appdraft.config import config
from flask_script._compat import text_type

configuracion=config["development"]
app = inicializar_app(configuracion)

manager = Manager(app)



if __name__ == '__main__':
    manager.run()
