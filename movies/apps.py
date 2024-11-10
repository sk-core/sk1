from django.apps import AppConfig


# 定义应用程序的配置类
class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # 指定默认的主键字段类型
    name = 'movies'  # 应用的名称，Django 使用此名称来识别应用
    verbose_name = '电影'  # 显示在 Django admin 中的应用名称

