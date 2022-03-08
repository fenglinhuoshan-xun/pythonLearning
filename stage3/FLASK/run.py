# 从flask模块中导入Flask类，Flask是用来创建应用的
from flask import Flask
# 实例化出来的一个对象就是一个Flask应用，在创建应用时，要指定当前模块的模块名，把当前的模块变成flask应用
app = Flask(__name__)

# 路由，是一个装饰器，就是用来帮助我们去定位一个视图函数的
@app.route('/')
@app.route('/index')
# 视图函数，视图在flask中都是以一个函数的方式显示的
# http://127.0.0.1:5000/
def hello_world():
    return '这是一个项目的首页'

# http://127.0.0.1:5000/mil
@app.route('/mil')
def mil_view():
    return '这是军事相关的页面'

# http://127.0.0.1:5000/internet
@app.route('/internet')
def internet_view():
    return '这是互联网相关的页面'

# http://127.0.0.1:5000/show/xxx/xxx
@app.route('/show/<name>/<int:age>')
def show_view(name,age): # 装饰器中的这个name，视图函数可以接收之后不用，但是不能不接收，否则报错
    return '%s is %s years old' % (name,age)


# 通过我们创建的应用，来启动一个flask的服务程序，它的功能就是启动了一个自带的小型服务器
# debug默认是关着的，设置degub=True，打开调试模式。这样子每当我们保存的时候，会自动的帮助我们刷新程序，如果代码出错，还会给我们提示
app.run(debug=True)
