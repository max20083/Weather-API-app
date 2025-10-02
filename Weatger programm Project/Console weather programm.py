import requests
while True:
    try:
     city_name=input('Введите город :')
     city_name=city_name.strip()
     API='b717851c0be44dfc87d2308760fae74d'
     zapr = requests.get('http://api.openweathermap.org/data/2.5/weather?',params={
         'q': city_name,
         'appid': API,
         'units': 'metric'
     })
     temperature = round(zapr.json()['main']['temp'])
     min_temp = round(zapr.json()['main']['temp_min'])
     max_temp = round(zapr.json()['main']['temp_max'])
     print(f'                        В городе {zapr.json()['name']}\nтемпература на данный момент составляет {temperature} градусов по цельсью \nминимальная температура за последние 24 часа составляет {min_temp} градусов по цельсию \nмаксимальная температура за последние 24 часа составляет {max_temp} градусов по цельсию\n                 (по версии openweathermap)')
    except KeyError:
        print('Неверно введен город попробуйте еще раз')