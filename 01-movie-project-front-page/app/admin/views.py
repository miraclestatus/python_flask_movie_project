# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 11:30
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : views.py
# @Software: PyCharm
from . import admin
@admin.route("/")
def index():
    return "<h1 style='color:green'>admin</h1>"