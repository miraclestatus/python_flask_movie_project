# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 11:30
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : views.py
# @Software: PyCharm
from . import home
from flask import render_template, redirect, url_for


@home.route("/")
def index():
    # return "<h1 style='color:red'>home</h1>"
    return render_template('home/index.html')
@home.route("/login/")
def login():
    return render_template('home/login.html')
@home.route("/logout/")
def logout():
    return redirect(url_for('home.login'))
@home.route("/regist/")
def regist():
    return render_template('home/register.html')
@home.route("/user/")
def user():
    return render_template("home/user.html")
