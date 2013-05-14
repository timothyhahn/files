import os.path
from flask import Flask
from flask.ext.autoindex import AutoIndex

app = Flask(__name__)
username = os.getlogin()
AutoIndex(app, browse_root=os.path.abspath('/home/' + username + '/public_files'))

if __name__ == '__main__':
        app.run()
