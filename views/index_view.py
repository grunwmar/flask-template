from flask import render_template
import helpers.config as config

def run():
    return render_template('content/index.html', content="Hello World!")
