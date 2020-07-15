# -*- coding: utf-8 -*- 
# @Time : 2020/7/14 12:54 AM 
# @Author : zhaotong 
# @File : Server.py

import flask
app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        p = flask.request.values.get("provice") # get方式
        c = flask.request.values.get("city") # 混合方式，get和post均可写成values接收
        note = flask.request.values.get("note") # post方式
        print(p,c)
        return p + "," + c + "\n" + str(note)
    except Exception as err:
        return str(err)
## 网页
# def index():
#     try:
#         fobj=open("index.htm","rb")
#         data=fobj.read()
#         fobj.close()
#         return data
#     except Exception as err:
#         return str(err)
# @app.route("/hi")
# def hi():
#     return "hi"
#
if __name__ == "__main__":
    app.run()