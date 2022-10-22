# import time
#
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# from config import TOKEN
# import os
# import requests
# import fake_useragent
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
import time
# driver = webdriver.Chrome(executable_path="geckodriver.exe")

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
#
# s=Service("chromedriver.exe")
# driver=webdriver.Chrome(service=s)
# driver.get('https://www.google.com')
# driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox("geckodriver.exe")

    # Navigate to url
driver.get("http://www.google.com")

    # Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)



time.sleep(5)

driver.close()
driver.quit()



# driver = webdriver.Chrome(executable_path=r"D:\Учеба\piton\ucheba\D_Z_git\chromedriver.exe", options=options)









# bot = Bot(TOKEN)
# dp = Dispatcher(bot)
#
# @dp.message_handler()
# async  def echo_send(message : types.Message):
#     await message.answer(message.text)
#     # await message.reply(message.text)
#     # await bot.send_message(message.from_user.id, message.text)
#
#
# executor.start_polling(dp, skip_updates=True)
# https://vk-leaders.ru/
# https://vk.com/
# chromedriver.exe
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.3.886 Yowser/2.5 Safari/537.36
