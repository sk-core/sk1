from django.shortcuts import render,redirect  # 从 Django 的 shortcuts 模块导入 render 函数，用于渲染模板
from .models import Book,Review  # 从当前应用导入 Book 模型
from django.shortcuts import get_object_or_404  # 从 Django 的 shortcuts 模块导入 get_object_or_404 函数，用于获取对象或返回 404
from book.forms import ReviewForm
from django.contrib.auth.decorators import login_required

@login_required
def createbookreview(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'GET':
        return render(request, 'createbookreview.html', {'form': ReviewForm, 'book': book})
    else:  # 如果请求方法不是 GET，通常是 POST
        try:  # 尝试执行以下代码块
            form = ReviewForm(request.POST)  # 使用提交的 POST 数据创建 ReviewForm 实例
            newReview = form.save(commit=False)  # 不立即保存，获取评论实例
            newReview.user = request.user  # 将当前用户设置为评论的作者
            newReview.book = book  # 将当前书籍设置为评论的关联电影
            newReview.save()  # 保存评论到数据库
            return redirect('bookdetail', newReview.book.id)  # 重定向到书籍详情页面
        except ValueError:  # 捕获可能的值错误
            return render(request, 'createbookreview.html', {'form': ReviewForm, 'error': '非法数据'})  # 渲染表单页面，并显示错误信息



def bookdetail(request, book_id):  # 定义视图函数 bookdetail，接收请求和书籍 ID
    book = get_object_or_404(Book, pk=book_id)  # 尝试获取指定 ID 的书籍，如果不存在则返回 404
    reviews = Review.objects.filter(book=book)
    return render(request, 'bookdetail.html', {'book': book,'reviews':reviews},)  # 渲染 'bookdetail.html' 模板，并传递书籍对象

def bookhome(request):  # 定义视图函数 bookhome，接收请求
    searchTerm = request.GET.get('searchBook')  # 从 GET 请求中获取搜索关键字 'searchBook'
    if searchTerm:  # 如果存在搜索关键字
        books = Book.objects.filter(title__contains=searchTerm)  # 查询书籍标题中包含搜索关键字的所有书籍
    else:  # 如果没有搜索关键字
        books = Book.objects.all()  # 获取所有书籍
    return render(request, 'bookhome.html', {'searchTerm': searchTerm, 'books': books})  # 渲染 'bookhome.html' 模板，并传递搜索关键字和书籍列表

def updatebookreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatebookreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('bookdetail', review.book.id)
        except ValueError:
            return render(request, 'updatebookreview.html', {'review':review, 'form':form, 'error':'提交非法数据'})