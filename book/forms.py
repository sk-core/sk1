from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):  # 定义一个 ReviewForm 类，继承自 ModelForm
    def __init__(self, *args, **kwargs):  # 初始化方法，接受任意位置参数和关键字参数
        super(ReviewForm, self).__init__(*args, **kwargs)  # 调用父类初始化方法
        # 为 'text' 字段的输入框添加 CSS 类 'form-control'
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        # 为 'watchAgain' 字段的输入框添加 CSS 类 'form-check-input'
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:  # 定义元类 Meta，用于配置表单的选项
        model = Review  # 指定使用的模型是 Review
        fields = ['text', 'watchAgain']  # 指定表单中包含的字段
        labels = {  # 定义字段的标签，用于显示
            'text': ('说说你看过之后的感受吧...'),  # 'text' 字段的标签
            'watchAgain': ('是否会再次观看'),  # 'watchAgain' 字段的标签
        }
        widgets = {  # 定义字段的小部件选项
            'text': Textarea(attrs={'rows': 4}),  # 将 'text' 字段的输入框设置为 Textarea，并指定行数为 4
        }
