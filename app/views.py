from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import AfghanistanPopulation, User


# Create your views here.

class Index(View):

    @staticmethod
    def get(request):
        return render(request, 'afghanistan_overview.html')


def afghanistan_overview(request):
    # 在这里编写你获取阿富汗概况信息的逻辑
    country_name = "阿富汗"
    population = "38,928,346"
    capital = "喀布尔"
    language = "普什图语、达里语"
    currency = "阿富汗尼"
    # ... 其他信息或数据

    context = {
        'country_name': country_name,
        'population': population,
        'capital': capital,
        'language': language,
        'currency': currency,
        # ... 其他信息或数据
    }

    return render(request, 'afghanistan_overview.html', context)


def history(request):
    return render(request, 'history.html')


def diplomacy(request):
    return render(request, 'diplomacy.html')


def culture(request):
    return render(request, 'culture.html')


def output_all_entries(request):
    all_entries = AfghanistanPopulation.objects.all()
    return render(request, 'message.html', {'entries': all_entries})


def contact(request):
    return render(request, 'contact.html')


def map(request):
    return render(request, 'map.html')


def error(request):
    raise Http404(request, '404.html')


def review(request):
    return render(request, 'review.html')


def process_form(request):
    if request.method == 'POST':
        # 获取表单数据
        email = request.POST.get('email')

        # 创建一个新的User对象
        user = User(email=email)

        # 保存到数据库
        user.save()

        # 返回响应给客户端
        return HttpResponse('表单已成功提交')