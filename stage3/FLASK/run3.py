from flask import Flask,render_template,request

# 修改默认模板的目录，还有同时修改文件系统中的目录名称，F2重命名。我们还可以鼠标移Flask到类上，看一些下里面默认的参数
app = Flask(__name__,template_folder='temp')

@app.route('/')
def index_view():
    title = '<老王的幸福生活>'
    author = 'qtx,laowang'
    content = '老王5点起床，开车去公司上班，18点下班，开车下班'
    # render_template还可以传入另外的参数，字典形式传入，即模板变量=值
    return render_template('index.html',title=title,author=author,content=content)

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/show',methods=['POST','GET'])
def show_view():
    # request.args：保存的是get方式提交的数据
    # request.form：保存的是post方式提交的数据
    print(request.form) # ImmutableMultiDict([('uname', 'xun'), ('upwd', '123')]) 类似字段的结构，每一个元组表示的是一个键值对
    
    # return "用户登录成功，欢迎%s" % request.form['uname']
    return "用户登录成功，欢迎%s" % request.form.get('uname')
app.run(debug=True)