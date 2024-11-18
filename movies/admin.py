from django.contrib import admin
from movies.models import Movie,Review
# from .models import Department
# from .models import Student

admin.site.register(Review)
admin.site.register(Movie)
admin.site.site_header='minidouban后台管理'
admin.site.site_title='python web开发! '
