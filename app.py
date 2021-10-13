from flask import Flask
from flask import request
from period_number import Period_number

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api_ae/v1.0/period_number/group_by_site', methods=["POST"])
def group_by_site():
    data = request.get_json()
    new_var = Period_number()
    new_var2 = new_var.main(data)
    return new_var2


# @app.route('/api_ae/v1.0/period_number/group_by_date', methods=["POST"])
# def group_by_date():
#     data = request.get_json()
#     new_var = Period_number()
#     new_var2 = new_var.main(data)
#     return new_var2


if __name__ == '__main__':
    app.run()
