# coding:utf-8
from flask import Blueprint, render_template, request
from data import db
module = Blueprint(__name__.split('.')[-1], __name__)


@module.route("/")
def hello():
    host = request.headers.get('remote_addr')
    if not host:
        host = request.remote_addr
    if not db.ips.find_one({"ip": host}):
        print db.ips.insert({"ip": host})
    for ip in db.ips.find():
        print ip["ip"]
    return render_template("home/index.html", host=host, hosts=db.ips.find())
