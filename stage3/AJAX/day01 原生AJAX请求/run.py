from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)

@app.route('/get')
def get_request():
    print(request.args) # ImmutableMultiDict([('uname', 'xun'), ('upwd', '111')]) 类字典的结构
    # uname = request.args['uname'] # 通常会加一个异常处理，看字典里面有没有这个键
    uname = request.args.get('uname') # get方式如果没有数据，则默认显示为None，不会出异常
    return "欢迎%s" % uname

@app.route('/post',methods = ['POST'])
def post_view():
        print(request.form) # ImmutableMultiDict([('uname', 'xun'), ('upwd', '111')]) 类字典的结构
        # uname = request.form['uname']
        uname = request.form.get('uname')
        return "欢迎%s" % uname

@app.route('/demo',methods = ['GET','POST'])
def demo_view():
    print(request.method)
    if request.method == 'GET':
        # return render_template('demo2.html')
        return '获取get方式提交数据成功'
    elif request.method == 'POST':
        return "获取数据成功"

@app.route('/ajax')
def ajax_view():
    return render_template('demo3.html')

@app.route('/json',methods = ['GET','POST'])
def json_view():
    if request.method == 'GET':
        return render_template('demo4.html')
    elif request.method == 'POST':
        # form post 提交
        # key = request.form.get('key')
        # ajax json 提交
        # key = request.json.get('key') # 获取json格式的数据
        # 自定义状态码
        # 1001数据有用
        # 1002...
        jsonStr = json.dumps({'code':1001,'res':'数据有用'})
        return jsonStr

@app.route('/news')
def news_view():
    return render_template('exercise2.html')

@app.route('/news/all')
def all_views():
    news_list = [
        '民生发展',
        '养老服务',
        '多地民政局',
        '北上广春节',
    ]
    return json.dumps(news_list)

if __name__ == '__main__':
    app.run(debug=True)