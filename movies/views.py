from django.shortcuts import render, redirect
from django.http import HttpResponse
import os,django
from movies.models import Movie,Review
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from movies.forms import ReviewForm
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def createmoviereview(request, movie_id):  # 定义视图函数 createmoviereview，接收请求和电影 ID
    movie = get_object_or_404(Movie, pk=movie_id)  # 尝试获取指定 ID 的电影，如果不存在则返回 404
    if request.method == 'GET':  # 如果请求方法是 GET
        return render(request, 'createmoviereview.html', {'form': ReviewForm, 'movie': movie})  # 渲染创建评论的表单页面，并传递表单和电影对象
    else:  # 如果请求方法不是 GET，通常是 POST
        try:  # 尝试执行以下代码块
            form = ReviewForm(request.POST)  # 使用提交的 POST 数据创建 ReviewForm 实例
            newReview = form.save(commit=False)  # 不立即保存，获取评论实例
            newReview.user = request.user  # 将当前用户设置为评论的作者
            newReview.movie = movie  # 将当前电影设置为评论的关联电影
            newReview.save()  # 保存评论到数据库
            return redirect('moviedetail', newReview.movie.id)  # 重定向到电影详情页面
        except ValueError:  # 捕获可能的值错误
            return render(request, 'createmoviereview.html', {'form': ReviewForm, 'error': '非法数据'})  # 渲染表单页面，并显示错误信息

def home(request):  # 定义视图函数 home
    movies = Movie.objects.all()  # 从数据库获取所有电影
    return render(request, 'home.html', {'movies': movies})

def moviehome(request):  # 定义视图函数 moviehome
    searchTerm = request.GET.get('searchMovie')  # 从 GET 请求中获取搜索关键字 'searchMovie'
    if searchTerm:  # 如果存在搜索关键字
        movie_list = Movie.objects.filter(title__contains=searchTerm)  # 查询标题中包含搜索关键字的电影
    else:  # 如果没有搜索关键字
        movie_list = Movie.objects.all()  # 获取所有电影
    paginator = Paginator(movie_list, 2)  # 创建分页器，每页显示 2 部电影
    page_number = request.GET.get('page', 1)  # 从 GET 请求中获取当前页码，默认为 1
    movies = paginator.page(page_number)  # 获取当前页的电影
    return render(request, 'moviehome.html', {'searchTerm': searchTerm, 'movies': movies})  # 渲染电影主页模板，并传递搜索关键字和电影列表

def signup(request):  # 定义视图函数 signup
    email = request.GET.get('email')  # 从 GET 请求中获取邮箱
    return render(request, 'signup.html', {'email': email})  # 渲染注册页面，并传递邮箱

def moviedetail(request, movie_id):  # 定义视图函数 moviedetail，接收请求和电影 ID
    movie = get_object_or_404(Movie, pk=movie_id)  # 尝试获取指定 ID 的电影，如果不存在则返回 404
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'moviedetail.html', {'movie': movie,
                                                'reviews': reviews
                                                })  # 渲染电影详情模板，并传递电影对象
@login_required
def updatemoviereview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatemoviereview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('moviedetail', review.movie.id)
        except ValueError:
            return render(request, 'updatemoviereview.html', {'review':review, 'form':form, 'error':'提交非法数据'})
@login_required
def deletemoviereview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('moviedetail', review.movie.id)