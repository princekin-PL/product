from django.shortcuts import render,redirect
#导入一个模块来判断用户是否登录
from django.contrib.auth.decorators import login_required
from .models import Product
#自动获取时间的模块
from django.utils import timezone
# Create your views here.
def products_list(request):
    return render(request,'products_list.html')


@login_required()
def publish(request):
    if request.method == 'GET':
        return render(request,'publish.html')
    elif request.method == 'POST':
        title = request.POST['标题']
        intro    = request.POST['介绍']
        url      = request.POST['APP链接']
        try:
            icon     = request.POST['APP图标']
            image    = request.POST['大图']

            product = Product()
            product.title = title
            product.intro = intro
            product.url = url
            product.icon = icon
            product.image = image

            product.pub_time = timezone.datetime.now()
            product.hunter = request.user

            product.save()

            return redirect('主页')
        except Exception as err:
            return render(request,'publish.html',{'错误':'请上传图片'})