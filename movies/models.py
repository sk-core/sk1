from django.db import models  # 导入 Django 的模型模块，用于创建数据库模型
from django.contrib.auth.models import User  # 导入用户模型，用于与用户关联

class Movie(models.Model):  # 定义一个电影模型，继承自 Django 的 models.Model
    title = models.CharField(max_length=100, verbose_name="电影名")  # 定义电影名称字段，最大长度为 100，显示名称为“电影名”
    description = models.CharField(max_length=250, verbose_name="电影简介")  # 定义电影简介字段，最大长度为 250，显示名称为“电影简介”
    image_url = models.ImageField(upload_to='movie/images/', verbose_name="电影海报", null=True, blank=True)  # 定义电影海报字段，上传到指定目录，允许 null 和空值
    movie_url = models.URLField(blank=True, verbose_name="电影资源链接")  # 定义电影资源链接字段，允许空值，显示名称为“电影资源链接”

    class Meta:  # Meta 类用于定义模型的元选项
        verbose_name = "电影"  # 单数形式的显示名称为“电影”
        verbose_name_plural = "电影"  # 复数形式的显示名称为“电影”

    def __str__(self):  # 定义字符串表示方法
        return self.title  # 返回电影的标题

#这一行定义了一个名为 Review 的模型，继承自 models.Model。Django 会根据这个类创建一个数据库表
class Review(models.Model) :
    text = models.CharField(max_length=100)#定义了一个字符字段 text，用于存储评论内容，最大长度为 100 个字符。
    #定义了一个日期时间字段 date，自动记录评论创建的时间，auto_now_add=True 意味着在创建时自动设置当前时间。
    date = models.DateTimeField(auto_now_add=True)
    #定义了一个外键字段 user，与 User 模型关联，表示评论的作者。当用户被删除时，关联的评论也会被删除
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_reviews')
    #定义了一个外键字段 movie，与 Movie 模型关联，表示这条评论是针对哪部电影的。删除电影时，该电影的评论也会被删除。
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    #定义了一个布尔字段 watchAgain，用于表示用户是否愿意再次观看该电影
    watchAgain = models.BooleanField()
#   这个方法定义了当调用 str() 函数或在 Django Admin 界面中展示该对象时所返回的字符串。在这里，返回的是评论的文本内容。
    def __str__(self) :
        return self.text

