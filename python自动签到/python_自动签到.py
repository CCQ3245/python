#！/user/bin/python3
# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import csv

with open("签到表单.csv",'a',newline='') as f:
    csvwriter = csv.writer(f,dialect='excel')
    csvwriter.writerow(['名字','性别','电话','专业'])
# temp =
app = Flask (__name__)
@app.route('/')
def idex():
    return render_template('htmld.html')
@app.route('/s')
def log():
    return render_template('html2.html')
@app.route('/m')
def ok():
    name = request.args.get("name")
    sex = request.args.get("sex")
    iphone = request.args.get("iphone")
    classs = request.args.get("classs")
    print(name,sex,iphone,classs)
    with open("签到表单.csv",'a',newline='') as f:
        csvwriter = csv.writer(f,dialect='excel')
        # csvwriter.writerow(['名字','性别','电话','专业'])
        csvwriter.writerow([name,sex,iphone,classs])
    return render_template('html3.html')
app.run()
