#!/usr/bin/python3
# coding=utf-8
from flask import Flask,render_template,request,jsonify
import time
import RPi.GPIO as GPIO

app = Flask(__name__,static_folder='../static',template_folder='../templates')

def webconsole(_1553b):
    @app.route('/console',methods=['GET'])
    def console():
        return render_template('console.html')

    @app.route('/status',methods=['GET'])
    def set_status():
        action = request.values.get("action")
        # runing:启动边扫、吸尘、行走
        # pause:边扫、吸尘继续，行走暂停
        # stop: 边扫、吸尘、行走全部停止
        if action == 'runing':
            __power_on()
        if action == 'stop':
            __power_off()

        _1553b["STATUS"] = action
        return jsonify({'result': "success"})

    app.run(host="192.168.0.9",port=80,debug=False)


#BCM
power = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(power,GPIO.OUT,initial=GPIO.LOW)
def __power_on():
    GPIO.output(power,GPIO.HIGH)

def __power_off():
    GPIO.output(power,GPIO.LOW)