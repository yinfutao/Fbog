# coding:utf-8
from flask import Flask
import views
import data
import config

app = Flask(__name__)
app.config.from_object(config)

data.init(app)
views.init(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
