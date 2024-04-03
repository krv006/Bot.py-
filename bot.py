import telebot
import requests
from telebot import types
from telegram import ReplyKeyboardMarkup, KeyboardButton

# Initialize your bot with the Telegram token
bot = telebot.TeleBot("7199941527:AAH-MfUWCY7Rb3nZBC5oGhaNX1tjzuSrouE")

# Define your API base URL
API_BASE_URL = "http://127.0.0.1:8000/api/"

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, welcome to the Telegram Bot!")

# Handle the /categories command
@bot.message_handler(commands=['categories'])
def send_categories(message):
    categories_data = requests.get(API_BASE_URL + 'categories/').json()
    categories_list = [category['name'] for category in categories_data]
    # categories_string = '\n'.join(categories_list)
    # bot.reply_to(message, f'Available categories:\n{categories_string}')
    buttons = []
    for category in categories_list:
        button = KeyboardButton(category)
        buttons.append(button)

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    bot.reply_to(message, 'Choose a category:', reply_markup=keyboard)



@bot.message_handler(commands=['rv'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    k = types.KeyboardButton('salom')
    r = types.KeyboardButton('alik')
    markup.add(k,r)
    bot.reply_to(message, "Assalomu alaykum, botimizga xush kelibsiz!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I don't understand that command.")

bot.polling()
