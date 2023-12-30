# -*- coding: utf-8 -*-

import jiedaoxyz as jdxyz
import os
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect#重定向
from flask import abort #异常抛出
from flask import render_template #模板渲染
app = Flask(__name__)

SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))
GEO_JSON    = SOURCE_PATH + "/芝罘区.json"
# 对 url 中，/user/ 后面的内容进行匹配、截取，赋值给变量 name，默认匹配字符串，可以指定类型。例如，/user/<int:id> 只匹配 id 为整数的 URL
@app.route('/<name>')

def hello_world(name):#变量 name 作为参数传递给函数 user[关键字参数]
    #可以根据不同的name关键字做不同的处理逻辑
    if name == "print":
        p1 = request.args.get('p1', 1, type=float)#从 url 获取 键为 p1 的 值转换为整形，如果没有 或 转换失败，默认为 1
        p2 = request.args.get('p2', 1, type=float)
        return jdxyz.jiedao(GEO_JSON,p1,p2)
        
    elif name == "return":
        print(request.args)
        response = make_response('<h1>This document carries a cookie!</h1>')#采用Response 对象返回响应
        # response.headers()
        response.set_cookie('answer', '42') # 设置 cookie
        return response
        # return 'Hello World!' + "\t" + name
    elif name == "help":
        return render_template('help.html')
        #return redirect("http://baidu.com")#对该url进行重定向
    elif name == "test":
        return render_template('test.html')
    elif name == "notfind":
        print("not find")
        abort(404)#注意,abort 会直接跳出调用它的函数，抛出异常，把控制权交给 Web 服务器
    else:
        return "None"

if __name__ == '__main__':
    app.run()#它告诉Flask以开发模式运行你的网站以便于测试