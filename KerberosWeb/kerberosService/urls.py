from django.urls import path

from . import views


'''
path函数
path(route,view,kwargs,name)
route: route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns(kerverosWeb/urls) 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。
view: 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。
kwargs: 任意个关键字参数可以作为一个字典传递给目标视图函数。
name: 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。
'''
# python manage.py runserver 8080

urlpatterns = [
    path('api', views.API, name='API'),
]