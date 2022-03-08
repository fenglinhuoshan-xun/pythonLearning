from django.http import HttpResponse


def page_2003_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def page_view(request):
    html = "<h1>这是我的首页</h1>"
    return HttpResponse(html)


def page_1_view(request):
    html = "<h1>这是编号为1的网页<h2>"
    return HttpResponse(html)


def page_2_view(request):
    html = "<h1>这是编号为2的网页</h1>"
    return HttpResponse(html)


def pagen_view(request, pg):
    html = f"<h1>这是编号为{pg}的网页!</h2>"
    return HttpResponse(html)


def cal_view(request, n, op, m):
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse("Your op is wrong")

    result = 0
    if op == 'add':
        result = n + m
    elif op == 'sub':
        result = n - m
    elif op == 'mul':
        result = n * m

    return HttpResponse('结果为:%s' % result)


def cal2_view(request, x, op, y):
    html = 'x:%s op:%s y:%s' % (x, op, y)
    return HttpResponse(html)


def birthday_view(request, y, m, d):
    html = f"生日为{y}年{m}月{d}日"
    return HttpResponse(html)
