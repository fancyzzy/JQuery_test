#!/usr/bin/env python3


from flask import Flask
from flask import render_template
from flask import session
from flask import redirect, url_for
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():


    return render_template('yammer_rank.html', name = 'local_tester')


if __name__ == '__main__':


    app.run(debug=True)