from flask import Flask, request
import views
import helpers.config as config

app = Flask(__name__)


@app.route('/') # index
def index_view():
    return views.index_view.run()


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
