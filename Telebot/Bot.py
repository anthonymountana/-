import telebot
from congfig import TOKEN
from clasic import CryptoConverter, ConvertionExeption
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Чтобы начать работу введите: \n<имя валюты>, <валюта,'
'в которую хотите перевести>, <количество>')


@bot.message_handler(commands=['start'])
def info(message):
    bot.reply_to(message, f'Welcome, {message.chat.username} \nСписок доступных валют: биткоин, евро, рубль и доллар')



@bot.message_handler(content_types=['photo'])
def meme(message: telebot.types.Message):
    bot.reply_to(message, 'nice mem XDD')


@bot.message_handler(content_types=['text', ])
def answer(message: telebot.types.Message):
    try:
        values = message.text.split()

        if len(values) != 3:
            raise ConvertionExeption('неверное количество параметров параметров')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'ошибка пользователя \n{e}\nвведите команды /start и /help')
    except Exception as e:
        bot.reply_to(message, f'не удалось обработать команду \n{e}\nвведите команды /start и /help')
    else:
        text = f'Цена {amount} единиц "{quote}" в валюте "{base}" на данный момент: {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)