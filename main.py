import requests
from aiogram.types import InputFile
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging
from aiogram import Bot, Dispatcher, executor, types
import time


url = 'https://www.kinopoisk.ru/chance/'
# -----------------------------------------------------------------------------------

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token='1452519232:AAEGbfs_egzhyKJZkyJYMpOTtMneNmg-V7s')
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Создаем кнопки
    buttons = [
        types.InlineKeyboardButton(text='Случайный фильм', callback_data='rand_mov'),
        types.InlineKeyboardButton(text='Кнопка 2', callback_data='button2')
    ]
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    keyboard_markup.add(*buttons)

    await message.reply("Нажмите кнопку:", reply_markup=keyboard_markup)


# Обработчик нажатия кнопки
@dp.callback_query_handler()
async def process_callback_button(callback_query: types.CallbackQuery):
    # Получаем данные из нажатия кнопки
    button_data = callback_query.data

    # Отправляем сообщение обратно с информацией о нажатой кнопке
    # await bot.send_message(callback_query.from_user.id, f"Вы нажали кнопку: {button_data}")

    if button_data == 'rand_mov':
        service = Service(executable_path='/usr/bin/chromedriver')
        options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(service=service, options=options)
        driver = webdriver.Chrome(service=service, options=options)

        driver.maximize_window()

        try:
            # Загружаем страницу в веб-драйвере
            driver.get(url=url)
            time.sleep(2)
            # Находим и нажимаем кнопку
            input_element = driver.find_element(By.ID, 'search')
            input_element.click()
            # driver.get(url=url)

            soup = BeautifulSoup(driver.page_source, "html.parser")
            info = soup.find('div', class_='info')
            film_name = info.find('div', class_='filmName').text
            film_href = 'https://www.kinopoisk.ru/' + info.find('div', class_='filmName').find('a').get('href')
            about_film = soup.find('div', class_='syn').text

            await bot.send_message(callback_query.from_user.id, f"name: {film_name}\nhref: {film_href}\nabout: {about_film}")
            # print(f"name: {film_name}\nhref: {film_href}\nabout: {about_film}")
            # time.sleep(3)
        except Exception as _ex:
            print(_ex)
        finally:
            driver.close()
            driver.quit()
    elif button_data == 'button2':
        cat = InputFile("8bit.jpg")
        await bot.send_message(callback_query.from_user.id, 'Привет, Макар')
        await bot.send_photo(callback_query.from_user.id, photo=cat)
    # Ответить пользователю, что его нажатие кнопки обработано
    await callback_query.answer()


# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)