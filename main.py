import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

# masukan api key dan api token yang di butuhkan
openai.api_key = "sk-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"
bot = AsyncTeleBot('6219083756:AAGw0-Kjn-g7sw6dPW3e8OY7LRoutQdCcTA')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Halo salam kenal dengan saya burhan,ada yang bisa saya bantu?\
""")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    await bot.reply_to(message, response['choices'][0]['text'])


asyncio.run(bot.polling())
