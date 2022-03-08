from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index_view():
    return render_template('index.html',cid=1)

@app.route('/list/<int:cid>')
def list_view(cid):
    if cid <= 2:
        return '你传入的cid小于等于2'
    elif cid > 2:
        return '你传入的cid大于2'
    

app.run(debug=True)


