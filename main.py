import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def get_source_html(url):
    service = Service(executable_path='/usr/bin/chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    try:
        # Загружаем страницу в веб-драйвере
        driver.get(url=url)
        time.sleep(3)
        # Находим и нажимаем кнопку
        input_element = driver.find_element(By.ID, 'search')
        input_element.click()
        #driver.get(url=url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find('div', class_='info')
        film_name = info.find('div', class_='filmName').text
        film_href = 'https://www.kinopoisk.ru/' + info.find('div', class_='filmName').find('a').get('href')
        about_film = soup.find('div', class_='syn').text
        print(f"name: {film_name}\nhref: {film_href}\nabout: {about_film}")
        #time.sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()
def main():
    get_source_html('https://www.kinopoisk.ru/chance/')




if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------------
#
# # Установка уровня логирования
# logging.basicConfig(level=logging.INFO)
#
# # Инициализация бота и диспетчера
# bot = Bot(token='1452519232:AAEGbfs_egzhyKJZkyJYMpOTtMneNmg-V7s')
# dp = Dispatcher(bot)
#
#
# # Обработка команды /start
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     # Создаем объект клавиатуры
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#
#     # Создаем кнопки
#     button1 = types.KeyboardButton('Кнопка 1')
#     button2 = types.KeyboardButton('Кнопка 2')
#     button3 = types.KeyboardButton('Кнопка 3')
#
#     # Добавляем кнопки в клавиатуру
#     keyboard.add(button1, button2, button3)
#
#     # Отправляем сообщение с клавиатурой
#     await message.answer('Выберите пункт меню:', reply_markup=keyboard)
#
#
# # Обработка нажатий на кнопки
#
# @dp.message_handler(commands=['Кнопка 1'])
# async def button1(message: types.Message):
#     # rand = randint()
#     await bot.send_message('Твой фильм')
# @dp.message_handler(func=lambda message: True)
# async def buttons_handler(message: types.Message):
#     if message.text == 'Кнопка 1':
#         await message.answer('Вы выбрали кнопку 1')
#     elif message.text == 'Кнопка 2':
#         await message.answer('Вы выбрали кнопку 2')
#     elif message.text == 'Кнопка 3':
#         await message.answer('Вы выбрали кнопку 3')
#
#
# # Запуск бота
# if __name__ == '__main__':
#     from aiogram import executor
#
#     executor.start_polling(dp, skip_updates=True)







# import logging
# from aiogram import Bot, Dispatcher, executor, types
#
# API_TOKEN = '1452519232:AAEGbfs_egzhyKJZkyJYMpOTtMneNmg-V7s'
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     await message.reply("Привет\nЭтот бот случайно выберет фильм и облегчит тебе выбор\n/menu")
#
#
# @dp.message_handler(commands=['menu'])
# async def help_msg(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton('Кнопка 1')
#     button2 = types.KeyboardButton('Кнопка 2')
#     button3 = types.KeyboardButton('Кнопка 3')
#
#     keyboard.add(button1, button2, button3)
#
#     # Отправляем сообщение с клавиатурой
#     await message.answer('Выберите пункт меню:', reply_markup=keyboard)
#
# # Обработка нажатий на кнопки
# @dp.message_handler(func=lambda message: True)
# async def buttons_handler(message: types.Message):
#     if message.text == 'Кнопка 1':
#         await message.answer('Вы выбрали кнопку 1')
#     elif message.text == 'Кнопка 2':
#         await message.answer('Вы выбрали кнопку 2')
#     elif message.text == 'Кнопка 3':
#         await message.answer('Вы выбрали кнопку 3')
# @dp.message_handler(commands=['help'])
# async def help_msg(message: types.Message):
#
#     await message.reply("Для того чтобы получить ссылку на случайный фильм нажмите /menu")
#
# # @dp.message_handler()
# # async def echo(message: types.Message):
# #     # old style:
# #     # await bot.send_message(message.chat.id, message.text)
# #     await message.answer(message.text)
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)