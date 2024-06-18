from telebot import telegramBot
from ocrtest import *
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
TELEBOT_API_KEY = os.getenv("TELEBOT_API_KEY")
CHAT_ID = os.getenv("CHAT_ID")

client = OpenAI(api_key=OPEN_AI_KEY)

bot = telegramBot(TELEBOT_API_KEY, chatID=CHAT_ID)
img_name = "test1.jpg"
while True:
    res = bot.pollResponse(False, wait_time=999999)
    print(res['chatid'])
    if res['type'] == "image":
        print("image received")
        print(res['url'])
        bot.downloadImage(url = res['url'], filename=img_name)
        res = detect_text(img_name)
        bot.sendText(res)
        completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are a computer science professor ."},
            {"role": "user", "content": res}
        ])
        response = completion.choices[0].message.content
        print(response)
        bot.sendText(response)
    else:
        print('text received')
        print(res['content'])
        if res['content'] != "":
            prompt = res['content']
            print(prompt)
            completion = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are an operations employee in a biotech sales company."},
                {"role": "user", "content": prompt}
            ])
            response = completion.choices[0].message.content
            print(response)
            bot.sendText(response)