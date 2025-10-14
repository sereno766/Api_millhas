from flask import Flask
from routes.usuario_route import *

app = Flask(__name__)
app.register_blueprint(usuario_route)



if __name__ == "__main__":


    app.run(debug=True)