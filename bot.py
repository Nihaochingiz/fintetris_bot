import gspread
from datetime import date
import telebot 
gc = gspread.service_account()

bot_token = '5449036965:AAGAAac76mt6c8AkVW-8g3h6SbkNoJtExec'
bot = telebot.TeleBot(bot_token)


wks = gc.open("тестовые интеграции").sheet1

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 
"Привет, я бот для фиксирования затрат на интеграции с блоггерами. Напишите имя блогера и сколько было затрачено через дефис в формате [КАТЕГОРИЯ-ЦЕНА]:")
    

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        today = date.today().strftime("%d.%m.%Y")
        
        #  разделяем сообщение на 2 части, категория и цена
        blogger, price = message.text.split("-", 1)
        text_message = f'На {today} в таблицу расходов добавлена запись: блогер {blogger}, сумма {price} рублей'
        bot.send_message(message.chat.id, text_message)
        
        # открываем Google таблицу и добавляем запись
        wks.append_row([today, blogger, price])
    except:
        # если пользователь ввел неправильную информацию, оповещаем его и просим вводить повторно
        bot.send_message(message.chat.id, 'ОШИБКА! Неправильный формат данных!')
        
    bot.send_message(message.chat.id, 'Напишите имя блогера и сколько было затрачено через дефис в формате [КАТЕГОРИЯ-ЦЕНА]:')
    
if __name__ == '__main__':
     bot.polling(none_stop=True)