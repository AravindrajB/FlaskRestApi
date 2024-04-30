from flask import Flask
from Project.app.controllers.employee_controller import employee_bp
from Project.app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(employee_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
