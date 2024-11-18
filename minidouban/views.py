# views.py
from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse

def movie_info(request):
    return render(request, 'movie_info.html')
def generate_qr_code(request):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # 假设你的项目首页网址是http://your_domain/，你可以修改这个网址
    qr.add_data('http://47.96.37.182')
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')