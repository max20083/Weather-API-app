import requests
import time
from tkinter import *
from tkinter import Toplevel
login='Admin'
password='12345'
def clicked_auto():
    if login_entry.get() == login and password_entry.get() == password:
        status_lbl.configure(text='Успешный вход', fg='green')
        Autoriz_button.destroy()
        root=Toplevel(sign)
        root.title('Бот погоды')
        root.geometry('500x300')
        root.resizable(0,0)
        Hello_lbl=Label(root,text='Привет это программа для определения погоды в любой точке мире\n введи город и узнай какая там температура ')
        Hello_lbl.pack()
        city_entry=Entry(root)
        city_entry.pack(padx=10,pady=30)
        resp_button=Button(root,text='Узнать',width=10, command= lambda: clicked_request(city_entry,resp_lbl))
        resp_button.pack()
        resp_lbl=Label(root,text='',padx=10,pady=10)
        resp_lbl.pack()
    else:
        status_lbl.configure(text='Неверный логин или пароль', fg='red')
def clicked_request(city_entry,resp_lbl):
    resp_lbl.configure(text='Выполняется запрос......',fg='black')
    resp_lbl.update()
    time.sleep(0.5)
    try:
        city=city_entry.get()
        city=city.strip()
        API='b717851c0be44dfc87d2308760fae74d'
        zapr = requests.get('http://api.openweathermap.org/data/2.5/weather?', params={
            'q': city,
            'appid': API,
            'units': 'metric'
        })
        temperature = round(zapr.json()['main']['temp'])
        min_temp = round(zapr.json()['main']['temp_min'])
        max_temp = round(zapr.json()['main']['temp_max'])
        resp_lbl.configure(text=f'В городе {zapr.json()['name']}\nтемпература на данный момент составляет {temperature} градусов по цельсью \nминимальная температура ожидаемая на завтра составляет {min_temp} градусов по цельсию \nмаксимальная температура ожидаемая на завтра составляет {max_temp} градусов по цельсию\n(по версии openweathermap)',fg='black')
    except KeyError:
        resp_lbl.configure(text='Такого города не найдено попробуйте еще раз', fg='red')

sign = Tk()
sign.title('Авторизация')
sign.geometry('300x200')
frame_login=Frame(sign)
frame_login.pack()
login_lbl = Label(frame_login, text='логин')
login_lbl.pack(side=LEFT,padx=0,pady=5)
login_entry = Entry(frame_login , width=10)
login_entry.pack(side=LEFT,padx=10,pady=5)
frame_password=Frame(sign)
frame_password.pack()
password_lbl = Label(frame_password, text='пароль')
password_lbl.pack(side=LEFT,padx=0,pady=0)
password_entry=Entry(frame_password , width=10)
password_entry.pack(side=LEFT,padx=10,pady=0)
frame_auto=Frame(sign)
frame_auto.pack()
Autoriz_button = Button(frame_auto, text='Войти', width=10,command=clicked_auto)
Autoriz_button.pack(side=LEFT, pady=30, padx=100)
frame_status=Frame(sign)
frame_status.pack()
status_lbl = Label(frame_status, text='')
status_lbl.pack(side=LEFT,padx=0,pady=0)


sign.mainloop()
