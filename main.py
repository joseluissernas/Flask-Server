from flask import Flask
from Routes.files import routes_files

app = Flask(__name__)

app.register_blueprint(routes_files)

@app.route('/')
def index():
    return "hola"
     
if __name__ == '__main__':
    app.run(debug=True, port="4000", host="0.0.0.0")
    
    
    
    

