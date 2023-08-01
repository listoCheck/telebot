import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6041166937:AAHv7754_Ikmy5q-y_SwZVPBL4kF1oHQKGE')


def download_image(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    link_array = ""
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        links = soup.find_all("a")
        for link in links:
            if "movie" in str(link):
                link_array += str(link).split(" ")[2].split('"')[1] + " "
    return link_array


######################################################################################
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("ДА!!!!")
    item2 = telebot.types.KeyboardButton("Нет.")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! '.format(message.from_user) + 'хочешь подрочить???',
                     reply_markup=markup)


###############################################################################################
@bot.message_handler(content_types=['text'])
def bot_message(message):
    user = message.from_user
    if message.chat.type == 'private':
        if message.text == "ДА!!!!":
            markup1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item0_0 = telebot.types.KeyboardButton("Оргии")
            item1_0 = telebot.types.KeyboardButton("Чулки")
            item2_0 = telebot.types.KeyboardButton("Анал")
            item3_0 = telebot.types.KeyboardButton("БДСМ")
            item4_0 = telebot.types.KeyboardButton("Блондинки")
            item5_0 = telebot.types.KeyboardButton("Большие сиськи")
            item1_1 = telebot.types.KeyboardButton("Большие члены")
            item2_1 = telebot.types.KeyboardButton("Брюнетки")
            item3_1 = telebot.types.KeyboardButton("В лосинах")
            item4_1 = telebot.types.KeyboardButton("В офисе")
            item5_1 = telebot.types.KeyboardButton("Групповое")
            item1_2 = telebot.types.KeyboardButton("Двойное проникновение")
            item2_2 = telebot.types.KeyboardButton("Домашнее")
            item3_2 = telebot.types.KeyboardButton("Дрочка")
            item4_2 = telebot.types.KeyboardButton("Жесткое")
            item5_2 = telebot.types.KeyboardButton("Жопы")
            item1_3 = telebot.types.KeyboardButton("Игрушки")
            item2_3 = telebot.types.KeyboardButton("Измена")
            item3_3 = telebot.types.KeyboardButton("Крупным планом")
            item4_3 = telebot.types.KeyboardButton("Массаж")
            item5_3 = telebot.types.KeyboardButton("Минет")
            item1_4 = telebot.types.KeyboardButton("Молодые")
            item2_4 = telebot.types.KeyboardButton("Оргазмы")
            item3_4 = telebot.types.KeyboardButton("Премиум")
            item4_4 = telebot.types.KeyboardButton("Русское")
            item5_4 = telebot.types.KeyboardButton("Секретарши")
            item1_5 = telebot.types.KeyboardButton("Студенты")
            item2_5 = telebot.types.KeyboardButton("Все категории")
            markup1.add(item0_0, item1_0, item2_0, item3_0, item4_0,
                        item5_0, item1_1, item2_1, item3_1, item4_1,
                        item5_1, item1_2, item2_2, item3_2, item4_2,
                        item5_2, item1_3, item2_3, item3_3, item4_3,
                        item5_3, item1_4, item2_4, item3_4, item4_4,
                        item5_4, item1_5, item2_5)
            bot.send_message(message.chat.id,
                             'Выбери интересующие тебя категории и я подберу самые новые и сочные видео))',
                             reply_markup=markup1)
        if message.text == "Анал":
            string = download_image("http://mob.porno365.expert/anal")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Анал", user.first_name, user.last_name)
        if message.text == "БДСМ":
            string = download_image("http://mob.porno365.expert/bds")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория БДСМ", user.first_name, user.last_name)
        if message.text == "Блондинки":
            string = download_image("http://mob.porno365.expert/blonde")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Блондинки", user.first_name, user.last_name)
        if message.text == "Большие сиськи":
            string = download_image("http://mob.porno365.expert/bolshie-siski")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Большие сиськи", user.first_name, user.last_name)
        if message.text == "Большие члены":
            string = download_image("http://mob.porno365.expert/big-cock")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Большие члены", user.first_name, user.last_name)
        if message.text == "Брюнетки":
            string = download_image("http://mob.porno365.expert/bryunetki")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Брюнетки", user.first_name, user.last_name)
        if message.text == "В лосинах":
            string = download_image("http://mob.porno365.expert/tights")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория В лосинах", user.first_name, user.last_name)
        if message.text == "В офисе":
            string = download_image("http://mob.porno365.expert/office")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория В офисе", user.first_name, user.last_name)
        if message.text == "Групповое":
            string = download_image("http://mob.porno365.expert/groupsex")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Групповое", user.first_name, user.last_name)
        if message.text == "Двойное проникновение":
            string = download_image("http://porno365.expert/dvoynoe-proniknovenie")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Двойное проникновение", user.first_name, user.last_name)
        if message.text == "Домашнее":
            string = download_image("http://ru.porno365.expert/domashnee")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Домашнее", user.first_name, user.last_name)
        if message.text == "Дрочка":
            string = download_image("http://ru.porno365.expert/handjob")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Дрочка", user.first_name, user.last_name)
        if message.text == "Жесткое":
            string = download_image("http://ru.porno365.expert/jestkoe")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Жесткое", user.first_name, user.last_name)
        if message.text == "":
            string = download_image("")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория ", user.first_name, user.last_name)
        if message.text == "Жопы":
            string = download_image("http://ru.porno365.expert/zhopy")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Жопы", user.first_name, user.last_name)
        if message.text == "":
            string = download_image("")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория ", user.first_name, user.last_name)
        if message.text == "Игрушки":
            string = download_image("http://ru.porno365.expert/toys")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Игрушки", user.first_name, user.last_name)
        if message.text == "Измена":
            string = download_image("http://ru.porno365.expert/izmena")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Измена", user.first_name, user.last_name)
        if message.text == "Крупным планом":
            string = download_image("http://ru.porno365.expert/close-up")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Крупным планом", user.first_name, user.last_name)
        if message.text == "Оргии":
            string = download_image("http://ru.porno365.expert/porno-orgii")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Оргии", user.first_name, user.last_name)
        if message.text == "Чулки":
            string = download_image("http://mob.porno365.expert/stockings")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Чулки", user.first_name, user.last_name)
        if message.text == "Массаж":
            string = download_image("http://ru.porno365.expert/%D0%BC%D0%B0%D1%81%D1%81%D0%B0%D0%B6")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Массаж", user.first_name, user.last_name)
        if message.text == "Минет":
            string = download_image("http://ru.porno365.expert/minet")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Минет", user.first_name, user.last_name)
        if message.text == "Молодые":
            string = download_image("http://ru.porno365.expert/minet")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Молодые", user.first_name, user.last_name)
        if message.text == "Оргазмы":
            string = download_image("http://ru.porno365.expert/orgazmy")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Оргазмы", user.first_name, user.last_name)
        if message.text == "Премиум":
            string = download_image("http://ru.porno365.expert/premium")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Премиум", user.first_name, user.last_name)
        if message.text == "Русское":
            string = download_image("http://ru.porno365.expert/russkoe")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Русское", user.first_name, user.last_name)
        if message.text == "Секретарши":
            string = download_image(
                "http://ru.porno365.expert/%D1%81%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D0%B0%D1%80%D1%88%D0%B8")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Секретарши", user.first_name, user.last_name)
        if message.text == "Студенты":
            string = download_image("http://ru.porno365.expert/studenty")
            sss = string.split(" ")
            for message1 in sss[:5]:
                bot.send_message(message.chat.id, message1)
            print("категория Студенты", user.first_name, user.last_name)
        if message.text == "Все категории":
            string = download_image("http://ru.porno365.expert/")
            sss = string.split(" ")
            for message1 in sss[:10]:
                bot.send_message(message.chat.id, message1)
            print("Все категории", user.first_name, user.last_name)


bot.polling(none_stop=True)
