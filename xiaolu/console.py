#!/usr/bin/python3
# coding=utf-8
from flask import Flask,render_template,request,jsonify

app = Flask(__name__,static_folder='../static',template_folder='../templates')

def webconsole(_1553b):
    @app.route('/console',methods=['GET'])
    def console():
        return render_template('console.html')

    @app.route('/status',methods=['GET'])
    def set_status():
        action = request.values.get("set")
        _1553b["STATUS"] = action
        return jsonify({'result': "success"})

    app.run(host="192.168.1.210",port=80,debug=False)