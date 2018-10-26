#!/usr/bin/env python3


from flask import Flask
from flask import render_template
from flask import session
from flask import redirect, url_for
from flask import jsonify, request


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('yammer_rank.html', name = 'local_tester')


@app.route('/process_ajax', methods=['POST'])
def process_ajax():

    group_id = request.form['sel_group']
    letter_num = request.form['letter_num']

    if group_id and letter_num:
        print("DEBUG all data available!, group_id: {}, letter_num: {}".format(group_id, letter_num))
        return jsonify({'group_id': group_id, 'letter_num': letter_num})

    return jsonify({'error': 'Missing data!'})



    return jsonify({})

if __name__ == '__main__':


    app.run(debug=True)