from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InputFile
import logging
import time


url = 'https://www.kinopoisk.ru/chance/'

logging.basicConfig(level=logging.INFO)

bot = Bot(token='1452519232:AAEGbfs_egzhyKJZkyJYMpOTtMneNmg-V7s')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    buttons = types.InlineKeyboardButton(text='Случайный фильм', callback_data='rand_mov'),

    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    keyboard_markup.add(*buttons)

    await message.reply("Привет, по всей видимости, ты хочешь слуйчайный фильм, ну тогда жми на кнопку👇", reply_markup=keyboard_markup)

@dp.callback_query_handler()
async def process_callback_button(callback_query: types.CallbackQuery):

    button_data = callback_query.data

    if button_data == 'rand_mov':
        service = Service(executable_path='/usr/bin/chromedriver')
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

        driver.maximize_window()

        try:
            driver.get(url=url)
            time.sleep(2)

            input_element = driver.find_element(By.ID, 'search')
            input_element.click()

            soup = BeautifulSoup(driver.page_source, "html.parser")
            info = soup.find('div', class_='info')
            film_name = info.find('div', class_='filmName').text
            film_href = 'https://www.kinopoisk.ru/' + info.find('div', class_='filmName').find('a').get('href')
            about_film = soup.find('div', class_='syn').text

            await bot.send_message(callback_query.from_user.id, f"Название: {film_name}\nСсылка: {film_href}\nКоротко о фильме: {about_film}")
        except Exception as _ex:
            print(_ex)
        finally:
            driver.close()
            driver.quit()

    await callback_query.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)