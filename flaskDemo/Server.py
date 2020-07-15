# -*- coding: utf-8 -*- 
# @Time : 2020/7/14 12:54 AM 
# @Author : zhaotong 
# @File : Server.py

import flask
import os
app = flask.Flask(__name__)

@app.route("/upload", methods=["POST"])
def uploadFile():
    msg = ""
    try:
        if "fileName" in flask.request.values:
            fileName = flask.request.values.get("fileName")
            data = flask.request.get_data() # 上传方法
            fojb = open("upload" + fileName, "wb")
            fojb.write(data)
            fojb.close()
            msg = "OK"
        else:
            msg = "没有按要求上传文件"
    except Exception as err:
        print(err)
        msg = str(err)
    return msg

@app.route("/down")
def download():
    msg = ""
    if "fileName" not in flask.request.values:
        return "图像.png"
    else:
        data = b""
        try:
            fileName = flask.request.values.get("fileName")
            print(fileName)
            if fileName != "" and os.path.exists(fileName):
                fobj = open(fileName, "rb")
                data = fobj.read()
                fobj.close()
            msg = "下载成功"
        except Exception as err:
            data = str(err).encode()
            msg = "下载失败"
            return data

        return msg # flask请求必须有返回值

# @app.route("/mix", methods=["GET", "POST"])
# def index():
#     try:
#         p = flask.request.values.get("provice") # get方式
#         c = flask.request.values.get("city") # 混合方式，get和post均可写成values接收
#         note = flask.request.values.get("note") # post方式
#         print(p,c)
#         return p + "," + c + "\n" + str(note)
#     except Exception as err:
#         return str(err)
#
# @app.route("/web")
# def index():
#     try:
#         fobj=open("index.htm","rb")
#         data=fobj.read()
#         fobj.close()
#         return data
#     except Exception as err:
#         return str(err)
#
# @app.route("/hi")
# def hi():
#     return "hi"

if __name__ == "__main__":
    app.run()