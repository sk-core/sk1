from django.shortcuts import render  # 从 Django 的 shortcuts 模块导入 render 函数，用于渲染模板
from .models import Book  # 从当前应用导入 Book 模型
from django.shortcuts import get_object_or_404  # 从 Django 的 shortcuts 模块导入 get_object_or_404 函数，用于获取对象或返回 404


def bookdetail(request, book_id):  # 定义视图函数 bookdetail，接收请求和书籍 ID
    book = get_object_or_404(Book, pk=book_id)  # 尝试获取指定 ID 的书籍，如果不存在则返回 404
    return render(request, 'bookdetail.html', {'book': book})  # 渲染 'bookdetail.html' 模板，并传递书籍对象

def bookhome(request):  # 定义视图函数 bookhome，接收请求
    searchTerm = request.GET.get('searchBook')  # 从 GET 请求中获取搜索关键字 'searchBook'
    if searchTerm:  # 如果存在搜索关键字
        books = Book.objects.filter(title__contains=searchTerm)  # 查询书籍标题中包含搜索关键字的所有书籍
    else:  # 如果没有搜索关键字
        books = Book.objects.all()  # 获取所有书籍
    return render(request, 'bookhome.html', {'searchTerm': searchTerm, 'books': books})  # 渲染 'bookhome.html' 模板，并传递搜索关键字和书籍列表
def homebook(request):
    books = Book.objects.all()
    return render(request,'homebook.html',{'book': books})