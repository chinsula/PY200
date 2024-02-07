from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from landing.forms import TemplateForm


class TemplView(View):
    def get(self, request):
        if request.method == "GET":
            return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму

        # Заголовок HTTP_X_FORWARDED_FOR используется для идентификации исходного IP-адреса клиента,
        # который подключается к веб-серверу через HTTP-прокси или балансировщик нагрузки.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP

        user_agent = request.META.get('HTTP_USER_AGENT')


        if form.is_valid():  # Проверили, что данные все валидные
            text = form.cleaned_data.get("text")  # Получили очищенные данные
            ret_date = form.cleaned_data.get("ret_date")
            pic_date = form.cleaned_data.get("pic_date")
            return JsonResponse(
                {"text": text, "ret_date": ret_date, "pic_date": pic_date, "ip": ip, "user_agent": user_agent},
                json_dumps_params={'ensure_ascii': False, 'indent': 4})

        return render(request, 'landing/index.html', context={"form": form})

def template_view(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')

    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            text = form.cleaned_data.get("text")  # Получили очищенные данные
            ret_date = form.cleaned_data.get("ret_date")
            pic_date = form.cleaned_data.get("pic_date")
            return JsonResponse(
                {"text": text, "ret_date": ret_date, "pic_date": pic_date},
                json_dumps_params={'ensure_ascii': False, 'indent': 4})

        return render(request, 'landing/index.html', context={"form": form})


def home_view(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')
