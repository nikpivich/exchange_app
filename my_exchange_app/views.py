
from django.shortcuts import render
import requests

def converter(request):

    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
        # Возвращаем шаблон конвертера
        return render(request=request, template_name='converter.html', context=context)
    if request.method == 'POST':

        # Сохраняем в переменные введенные данные с шаблонв по ключам( ключи указаны в скобках)
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)


        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'converted_amount': converted_amount
        }
        return render(request=request, template_name='converter.html', context=context)