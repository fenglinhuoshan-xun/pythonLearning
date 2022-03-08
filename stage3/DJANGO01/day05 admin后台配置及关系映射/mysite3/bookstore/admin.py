from django.contrib import admin
from .models import Book, Author


# Register your models here.

class BookManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['id', 'title', 'pub', 'price']
    # list_display_links：点哪个列，我能进入到数据的修改页，默认情况下，link加到了ID上了
    # 控制list_display中的字段，哪些可以链接到修改页。前提：list_display_links中的值必须是list_display里面的
    list_display_links = ['title']
    # 添加过滤器
    list_filter = ['pub']
    # 添加搜索框。会根据你输入的字，针对这个容器中的字段进行模糊查询
    search_fields = ['title']
    # 添加可在列表页编辑的字段，前提：list_editable中的值必须是list_display中的值，并且和list_display_links的值互斥
    list_editable = ['price']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
