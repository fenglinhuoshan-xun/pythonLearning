from flask import Flask,render_template,request
import json,time

app = Flask(__name__)

@app.route('/ajax_get')
def get_view():
    return render_template('demo1.html')

@app.route('/ajax_get_server')
def get_server():
    data = {'code':200,'msg':'获取数据成功'}
    # return json.dumps(data) # 转化为字符串，再返回。客户端必须要解析
    return data # flask 1.1.1版本中，允许直接返回字典。客户端不用解析 

@app.route('/ajax_post')
def post_view():
    return render_template('demo2.html')

@app.route('/ajax_post_server',methods = ['POST'])
def post_server():
    age = request.form.get('age')
    if int(age) > 120:
        return {'code':201,'msg':'so big'}
    return {'code':200,'msg':'ok'}

@app.route('/ajax')
def ajax_view():
    return render_template('demo3.html')

@app.route('/ajax_server',methods = ['GET','POST'])
def ajax_server():
    if request.method == 'GET':
        time.sleep(2)
        return '获取get方式数据成功'
    elif request.method == 'POST':
        # 默认表单方式post提交
        # key = request.form.get('key')
        key = request.json.get('key')
        print('获取数据%s' % key)
        return '获取post方式数据成功'

@app.route('/cors_js')
def js_view():
    print(request.args) # ImmutableMultiDict([('uname', 'Maria'), ('callback', 'fun')])
    uname = request.args.get('uname')
    callback = request.args.get('callback')
    # 'fun("欢迎xxx")'
    return callback + '("欢迎%s")' % uname

@app.route('/exer')
def exer_view():
    data = [
        {"id":1001,"title":"今天天气不错1"},
        {"id":1002,"title":"今天天气不错2"},
        {"id":1003,"title":"今天天气不错3"},
        {"id":1004,"title":"今天天气不错4"},
    ]
    callback = request.args.get('callback')
    dataStr = json.dumps(data)
    return callback + '('+dataStr+')'

# 创建页面
# 向http://127.0.0.1:5000/exer发送跨域请求
# 请求成功时，将dataStr数据获取到，遍历显示到页面上

@app.route('/login')
def login_view():
    return render_template('exercise2.html')

@app.route('/login_server',methods = ['POST'])
def login_server():
    print(request.form)
    uname = request.form.get('uname')
    if not uname:
        return {"code":1001,"msg":"请输入用户名"}
    upwd = request.form.get('upwd')
    if not upwd:
        return {"code":1002,"msg":"请输入密码"}

    if uname == 'qtx' and upwd == '123456':
        return {"code":200,"msg":"登录成功"}
    else:
        return {"code":1003,"msg":"用户名或密码错误"}

if __name__ == '__main__':
    app.run(debug=True)


