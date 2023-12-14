import telebot

bot = telebot.TeleBot('6470533870:AAHOPcRkkzKTPsThu6ViaOJKZeU0fQIcgCs')
chat_id = 758700579
# @mafioso_game_bot

def send_message(message):
    bot.send_message(chat_id, f'Поздравляю, вы ||{message}||', parse_mode='MarkdownV2')
