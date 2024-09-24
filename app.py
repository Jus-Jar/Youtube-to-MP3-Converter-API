from flask import Flask
from views import views

def add_views(app):
    for view in views:
        app.register_blueprint(view)

app = Flask(__name__)
add_views(app)

if __name__ == '__main__':
    app.run(debug=True)

