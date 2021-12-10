import telebot, wikipedia, re
from telebot import types

token = "2131577582:AAG0gPUxFduEDlRQ51uJzuSCDMK6G0MVE30"

bot = telebot.TeleBot(token)

wikipedia.set_lang("ru")


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ("==" in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + "."
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return "Нет информации, прошу прощения."


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("МТУСИ", "/help", "облако", "ответы")
    bot.send_message(message.chat.id, 'Привет! Спроси меня что я умею.', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '''Я могу:
    1. Показывать свежую информацию о МТУСИ
    2. Отправить ссылку на облако с полезными ресурсами
    3. Также можете спросить меня о чём угодно в свободном порядке.    
    ''')


@bot.message_handler(content_types=['text'])
def answer(message):
    a = message.text.lower()
    if a == "мтуси":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif a == "облако":
        bot.send_message(message.chat.id,
                         'Псс, у меня есть немного полезной инфы для тебя. Иди за мной : https://drive.google.com/drive/folders/16abToWN02Pi9oFHISK64YP_k0pJNJHRx?usp=sharing')
    elif a == "ответы":
        bot.send_message(message.chat.id,
                         'Если у вас есть вопросы без ответов, то наверняка вам поможет гугл! Но я не совсем ленивый, так что спрошу на вики. Пишите запрос с добаллением знака вопроса, поиск ведётся по заголовкам википедии')
    elif a[len(a) - 1] == "?":
        bot.send_message(message.chat.id, getwiki(message.text))


bot.polling(none_stop=True)
