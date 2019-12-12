# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 11:28
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views