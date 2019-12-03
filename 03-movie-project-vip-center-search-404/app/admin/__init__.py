 # -*- coding: utf-8 -*-
# @Time    : 2019/11/26 11:28
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : __init__.py.py
# @Software: PyCharm
# coding:utf8
from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views