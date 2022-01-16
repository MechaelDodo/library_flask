from flask import Flask
from flask_script import Manager

app = Flask(__name__)
app.debug = True
manager = Manager(app)

if __name__=="__main__":
    manager.run()
