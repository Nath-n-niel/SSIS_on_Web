from flask import Flask, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from app.config import Config
from app.Models import Student
from app.Models import College
from app.Models import Course
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    csrf = CSRFProtect(app)
    # Session(app)


    from app.Routes import collegebp
    app.register_blueprint(collegebp, url_prefix='/college')

    from app.Routes import coursebp
    app.register_blueprint(coursebp, url_prefix='/course')

    from app.Routes import studentbp
    app.register_blueprint(studentbp, url_prefix='/student')

    @app.route('/')
    @app.route('/base')
    def index():
        return render_template('base.html')
    
    return app