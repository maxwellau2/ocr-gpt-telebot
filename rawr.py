from telebot import telegramBot

bot = telegramBot("", chatID="")
while True:
    res = bot.pollResponse(False, wait_time=30)
    print(res)