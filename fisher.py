from flask import Flask
from config import DEBUG

app = Flask(__name__)


# @app.route('/hello')
def hello():
    # 基于类的视图 (即插视图)
    return 'hello,zzw!'


app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    app.run(debug=DEBUG)
