from tkinter import *
import requests

# Создаем окно приложения
root = Tk()

# Функция, которая срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    # Получение данных полбзователя
    city = cityField.get()

    # API ключ
    key = '70e4b501b822581c7fd58e5a6321ff85'
    # Ссылка с которой получаем информацию в JSON формате
    url = 'http://api.openweathermap.org/data/2.5/weather'
    # Доп.параметры (ключ, ед. измерения, город, указанный пользователем
    parameters = {'APPID': key, 'q': city, 'units': 'metric'}
    # Отправка запроса по определенному URL
    result = requests.get(url, params=parameters)
    # Получение ответа в формате JSON
    weather = result.json()
    # Полученную информацию переносим в текстовую надпись для юзера
    info_tablo['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'

# Настраиваем главное окно
# Цвет фона
root['bg'] = '#fafafa'
# Название приложения
root.title('Погода Для Народа')
# Размеры окна
root.geometry('300x250')
# Измненение размеров окна
root.resizable(width=False, height=False)

# Создаем область размещения других объектов
# Указываем к какому окну принадлежит, его фон и обводку
frame_top = Frame(root, bg='#ffb700', bd=5)
# Указываем расположение
frame_top.place(relx=0.15, relwidth=0.7, relheight=0.25)

# Создаем вторую область размещения объектов с теми же параметрами
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relheight=0.1)

# Создаем поле для получения данных юзера
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack() # Размещение данного объекта ВСЕГДА нужно прописывать

# Создаем кнопку при нажатии которой будет срабатывать "get_weather"
btn = Button(frame_top, text='Посмотреть народу про погоду', command=get_weather)
btn.pack() # размещаем объект кнопка



