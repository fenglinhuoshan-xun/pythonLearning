from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名', max_length=11)


class Book(models.Model):
    title = models.CharField('书名', max_length=11)
    # 多对多属性的命名建议这样写：对面的类名小写的复数
    authors = models.ManyToManyField(Author)
