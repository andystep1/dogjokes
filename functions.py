from aiogram import Bot, types
from bs4 import BeautifulSoup
import requests

def get_anek():
    anekiUrl = 'https://baneks.ru/random'
    anekidoc = requests.get(anekiUrl).text
    anekisoup = BeautifulSoup(anekidoc, 'html.parser')
    anek = [x.get_text() for x in anekisoup.find_all('p')]
    return anek[0]

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    dogbutton = types.KeyboardButton("🐕")
    roflbutton = types.KeyboardButton("🤣")
    dogandroflbutton = types.KeyboardButton("🐕 🤣")
    keyboard.add(dogbutton)
    keyboard.add(roflbutton)
    keyboard.add(dogandroflbutton)
    return keyboard

def get_dog():
    dogUrl = 'https://dog.ceo/api/breeds/image/random'
    dogDoc = requests.get(dogUrl).json()
    return str(dogDoc['message'])

    
get_anek()
#https://baneks.ru/random