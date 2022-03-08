import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User


# Create your views here.
def reg_view(request):
    # 注册
    if request.method == 'GET':
        # GET   返回页面
        return render(request, 'user/register.html')
    elif request.method == 'POST':  # 其实还应该检查一下用户名中有没有违禁字，这个需要强大的词库才可以，这里就不做了
        # POST  处理提交数据
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        # 1. 两个密码要保持一致
        if password_1 != password_2:
            return HttpResponse('两次密码输入不一致')

        # 哈希算法：给定明文，计算出一段定长的，不可逆的密文 md5,sha-256都可以做出这种效果
        # 不可逆就是你就是看到密文，你也不可能算出明文
        # 特点
        # 1. 定长输出：不管明文输出长度多少，哈希值都是定长的，如：md5：不管你给我的明文是什么，md5算法生成的密文都是32位16进制的
        # 所有通常我们会根据md5算法生成的密文的长度来决定数据库中字段的长度限制
        # 2. 不可逆：无法反向计算出 对应的 明文
        # 3. 雪崩效应：输入只要改变，输出必变，而且变的特别夸张
        # 场景：1. 密码处理 2. 文件的完整性校验

        # 如何使用
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()

        # 2. 当前用户名是否可用
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名已注册')
        # 3. 插入数据【明文处理密码】
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            # 有可能报错，重复插入，唯一索引，注意并发写入问题
            print('--create user error %s' % (e))

        # 免登录一天
        request.session['username'] = username
        # 主键查询一定比其他所有快
        request.session['uid'] = user.id
        # 修改session存储时间为1天，默认14天

        return HttpResponseRedirect('/index')


def login_view(request):
    if request.method == 'GET':
        # 获取登录页面
        # 检查登录状态，如果登录了，显示已登录
        if request.session.get('username') and request.session.get('uid'):
            return HttpResponse('已登录')
        # 检查Cookies
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            # 回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')

        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 处理数据
        username = request.POST['username']
        password = request.POST['password']
        # 两种方案：
        # 1. 先查用户，再比对密码是否一致
        # 2. 先比对密码，再用and查询
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s' % (e))
            return HttpResponse('您的用户名或密码有误')  # 给个模糊的提示，防止有人居心叵测暴力破解

        # 比对密码
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('您的用户名或密码有误')

        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        # resp = HttpResponse('---登录成功---')
        resp = HttpResponseRedirect('/index')
        # 判断用户是否勾选了“记住用户名”
        # 勾选了 --> Cookies存储，username,uid，时间3天
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600 * 24 * 3)
            resp.set_cookie('uid', user.id, 3600 * 24 * 3)
        return resp


def logout_view(request):
    # 删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']

    resp = HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
