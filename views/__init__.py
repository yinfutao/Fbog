# coding:utf-8
from importlib import import_module

MODULES = ["user"]


def init(app):
    for name in MODULES:
        blueprint = import_module("." + name, __name__).module
        app.register_blueprint(blueprint)
