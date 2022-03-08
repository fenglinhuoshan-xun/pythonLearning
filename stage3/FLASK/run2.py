from flask import Flask,request,url_for # 所有和请求有关的内容，都会保存在flask模块中提供的request对象中

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index_view():
    print(request.method) # 打印当前请求的类型
    if request.method == 'GET':      
        return '<form method="POST" action="/">'\
            '<input type="submit">'\
                '</form>'
    elif request.method == 'POST':
        return 'POST请求的数据提交成功'

@app.route('/user/<uname>')
def uname_view(uname):
    return '%s有关的信息' % uname

@app.route('/urlFor')
def url_view():
    return '反向解析qtx有关信息的地址是%s' % url_for('uname_view',uname = 'qtx')

app.run(debug=True)

