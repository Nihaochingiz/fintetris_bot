
import re
import telebot
from telebot import types
import time
bot = telebot.TeleBot("5561102690:AAF_cONTvU8anJahcXKxBGRCigPtCgOYn54")
keyboard = telebot.types.InlineKeyboardMarkup()

pattern = "(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})"


@bot.message_handler(commands=['start', 'фт'])
def start(message):
    mess = f'Здравствуйте! Хотите получить бесплатный чек лист "7 вопросов себе для создания капитала"или узнать подробнее о курсе"Финансовый тетрис начните отвечать боту Да"?'
    bot.send_message(message.chat.id,mess,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Узнать о курсе')
    itembtn2 = types.KeyboardButton('Получить чек-лист')
    markup.add(itembtn1, itembtn2 )
    bot.send_message(message.chat.id, "Кликните на подходящую кнопку ниже:", reply_markup=markup)
@bot.message_handler()
def get_checklist(message):
    message_checklist = f'Чек-лист "7 вопросов себе для создания капитала" поможет вам научиться:'\
            '- создавать капитал 💰;'\
            '- получать доход от капитала;'\
            '- грамотно управлять им;'\
            '- и защищать капитал.'\

    bot.send_message(message.chat.id,message_checklist ,parse_mode='html')
    if message.text == 'Узнать о курсе':
        quiz(message)
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Получить чек-лист', url='https://drive.google.com/file/d/1f81hGXLWmJKj2G5c1q5E_ktWiKwe7-Pu/view')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Чтобы его получить, кликните на кнопку ниже 👇", reply_markup = markup)

    time.sleep(2)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    how = f'Ну как? Вы уже изучили чек-лист'
    sent_how_message = bot.send_message(message.chat.id,how,parse_mode='html')
    bot.register_next_step_handler( sent_how_message ,  question_before_quiz)

def bye_before_quiz(message):
    message = f' Хорошо. Уверена, что на моем аккаунте вы найдете еще много полезной информации 😉'
    bot.send_message(message.chat.id,message,parse_mode='html')
    
def question_before_quiz(message):
        message_before_quiz = f'Наверняка после прочтения у вас в мыслях уже начинает потихоньку зарождаться личный инвестиционный план.'\
            'Чтобы выстроить свою правильную финансовую модель и обеспечить комфортную жизнь себе и своим потомкам, нужно погрузиться в эту тему с головой. 👨‍💻'\
            '📝Об этом максимально подробно и попунктам мы рассказываем на курсе'\
            '- находим дополнительные источники дохода;- выбираем стратегии финансового роста- создаём систему планомерных накоплений- выстраиваем щит от потерь.Хотите получить бесплатную консультацию от эксперта?'\

        bot.send_message(message.chat.id,message_before_quiz  ,parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Да')
        itembtn2 = types.KeyboardButton('Нет')
        markup.add(itembtn1, itembtn2 )
        free = f'Хотите бесплатную помощь эксперта?'
        sent_free_message = bot.send_message(message.chat.id,free,parse_mode='html')
        bot.register_next_step_handler( sent_free_message,  quiz)


        

def denied_question_before_quiz(message):
        denied_message_before_quiz = f'Хорошо, нажмите кнопку ниже, как'\
            'только прочитаете его 👇'\
            'Я дам вам еще немного информации '\
            'в дополнение к нему.'\

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Я прочитал(-а)')
        markup.add(itembtn1)
        bot.send_message(message.chat.id, denied_message_before_quiz , reply_markup=markup)
        if message.text == "Я прочитал(-а)":
           question_before_quiz(message)

def are_you_sure(message):
    message_are_you_sure = f'Вы уверены?'
    #bot.send_message(message.chat.id,message_are_you_sure,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Да')
    itembtn2 = types.KeyboardButton('Нет, я передумал')
    markup.add(itembtn1, itembtn2 )
    if message.text == "Да":
        denied_question_before_quiz(message)
    else:
        bot.register_next_step_handler(message_are_you_sure,quiz)






def quiz(message):
    question = f'Ответьте на 3 вопроса ниже и эксперт, '\
            'работающий по технологии «Финансовый'\
            'тетрис» проконсультирует вас 👇'\

    bot.send_message(message.chat.id,question,parse_mode='html')

    first_question(message)




def first_question(message):
    global user_data
    user_data = []
    question= f'1. Есть план финансового развития на 5 лет'\
            '2. Я не планирую долгосрочно'\
            '3. Моих ресурсов хватает только на месяц'\
            '4. Действую по обстоятельствам'\
            
                
    first_sent_question_message = bot.send_message(message.chat.id,question,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    itembtn4 = types.KeyboardButton('4')
    markup.add(itembtn1, itembtn2,itembtn3,itembtn4 )
    bot.send_message(message.chat.id, "Кликните на подходящую кнопку ниже:", reply_markup=markup)
    bot.register_next_step_handler( first_sent_question_message, second_question)


def second_question(message):
    global answer_first_question
    answer_first_question = ''
    if message.text == '1':
        answer_first_question += 'Есть план финансового развития на 5 лет'
    elif message.text == '2':
            answer_first_question += 'Я не планирую долгосрочно'
    elif message.text == '3':
           answer_first_question += 'Моих ресурсов хватает только на месяц'
    elif message.text == '4':
           answer_first_question += 'Действую по обстоятельствам'
    print(answer_first_question)
    user_data.append(answer_first_question)
    print(user_data)
    question= f'1. Я легко принимаю важные решения'\
            '2. Мои решения зачастую зависят от чужого мнения'\
            '3. Не умею говорить “нет”, поэтому накапливается внутренний негатив'\
            '4. Мне сложно найти решение, пугают перемены'\
                
    second_sent_question_message = bot.send_message(message.chat.id,question,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    itembtn4 = types.KeyboardButton('4')
    markup.add(itembtn1, itembtn2,itembtn3,itembtn4  )
    bot.send_message(message.chat.id, "Кликните на подходящую кнопку ниже:", reply_markup=markup)

    bot.register_next_step_handler( second_sent_question_message, third_question)



def third_question(message):
    global answer_second_question
    answer_second_question = ''
    if message.text == '1':
        answer_second_question += ' Я легко принимаю важные решения'
    elif message.text == '2':
            answer_second_question += 'Мои решения зачастую зависят от чужого мнения'
    elif message.text == '3':
            answer_second_question += 'Не умею говорить “нет”, поэтому накапливается внутренний негатив'
    elif message.text == '4':
           answer_second_question += 'Мне сложно найти решение, пугают перемены'
    print(answer_second_question)
    user_data.append(answer_second_question)
    print(user_data)
    question= f'1. У меня всегда есть подушка безопасности'\
            '2. Я живу от зарплаты до зарплаты'\
            '3. Мои расходы превышают доходы'\
            '4. За последний год у меня накопились долги'\
                
    third_sent_question_message = bot.send_message(message.chat.id,question,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    itembtn4= types.KeyboardButton('4')
    markup.add(itembtn1, itembtn2,itembtn3,itembtn4 )
    bot.send_message(message.chat.id, "Кликните на подходящую кнопку ниже:", reply_markup=markup)

    bot.register_next_step_handler( third_sent_question_message, get_sales)

def get_sales(message):
    global answer_third_question
    answer_third_question = ''
    if message.text == '1':
        answer_third_question += 'У меня всегда есть подушка безопасности'
    elif message.text == '2':
            answer_third_question += 'Я живу от зарплаты до зарплаты'
    elif message.text == '3':
           answer_third_question += 'Мои расходы превышают доходы'
    elif message.text == '4':
           answer_third_question += 'За последний год у меня накопились долги'
    print(answer_third_question)
    user_data.append(answer_third_question)
    print(user_data)
    lid_message = f'С вами свяжется мой помощник и расскажет все о курсе. Напишите ваш номер телефона'
    sent_get_message = bot.send_message(message.chat.id,lid_message,parse_mode='html')
    bot.register_next_step_handler(sent_get_message ,  get_user_phone)
def get_user_phone(message):
    global user_phone, pattern
    if re.fullmatch(pattern, message.text):
        get_user_name(message)
    else:
        msg = bot.send_message(message.chat.id, "Напишите номер в формате 8XXXXXXXXXX")
        bot.register_next_step_handler(msg,  get_user_phone)

def get_user_name(message):
            get_name = bot.send_message(message.chat.id,'Напишите ваше имя',parse_mode='html')
            user_phone = message.text
            user_data.append( user_phone )
            bot.register_next_step_handler(get_name,  say_bye)

def say_bye(message):
            bot.send_message(message.chat.id,'Спасибо за информацию. До свидания, с вами свяжется специалист',parse_mode='html')
            user_name = message.text
            user_data.append(user_name)
            print(user_data)
'''
#bot

def start(message):
    mess = f'Здравствуйте! Хотите получить бесплатный чек лист "7 вопросов себе для создания капитала"или узнать подробнее о курсе"Финансовый тетрис"?'
    bot.send_message(message.chat.id,mess,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Узнать о курсе')
    itembtn2 = types.KeyboardButton('Получить чек-лист')
    markup.add(itembtn1, itembtn2 )
    bot.send_message(message.chat.id, "Кликните на подходящую кнопку ниже:", reply_markup=markup)
@bot.message_handler()
def get_checklist(message):
    message_checklist = f'Чек-лист "7 вопросов себе для создания капитала" поможет вам научиться:'\
            '- создавать капитал 💰;'\
            '- получать доход от капитала;'\
            '- грамотно управлять им;'\
            '- и защищать капитал.'\

    bot.send_message(message.chat.id,message_checklist ,parse_mode='html')
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Получить чек-лист', url='https://drive.google.com/file/d/1f81hGXLWmJKj2G5c1q5E_ktWiKwe7-Pu/view')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Чтобы его получить, кликните на кнопку ниже 👇", reply_markup = markup)

    time.sleep(2)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    how = f'Ну как? Вы уже изучили чек-лист'
    sent_how_message = bot.send_message(message.chat.id,how,parse_mode='html')
    bot.register_next_step_handler( sent_how_message ,  question_before_quiz)
    
def question_before_quiz(message):
        message_before_quiz = f'Наверняка после прочтения у вас в мыслях уже начинает потихоньку зарождаться личный инвестиционный план.'\
            'Чтобы выстроить свою правильную финансовую модель и обеспечить комфортную жизнь себе и своим потомкам, нужно погрузиться в эту тему с головой. 👨‍💻'\
            '📝Об этом максимально подробно и попунктам мы рассказываем на курсе'\
            '- находим дополнительные источники дохода;- выбираем стратегии финансового роста- создаём систему планомерных накоплений- выстраиваем щит от потерь.Хотите получить бесплатную консультацию от эксперта?'\

        bot.send_message(message.chat.id,message_before_quiz  ,parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Да')
        itembtn2 = types.KeyboardButton('Нет')
        markup.add(itembtn1, itembtn2 )
        free = f'Хотите бесплатную помощь эксперта?'
        sent_free_message = bot.send_message(message.chat.id,free,parse_mode='html')
        bot.register_next_step_handler( sent_free_message,  quiz)
        

def denied_question_before_quiz(message):
        denied_message_before_quiz = f'Хорошо, нажмите кнопку ниже, как'\
            'только прочитаете его 👇'\
            'Я дам вам еще немного информации '\
            'в дополнение к нему.'\

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Я прочитал(-а)')
        markup.add(itembtn1)
        bot.send_message(message.chat.id, denied_message_before_quiz , reply_markup=markup)
        if message.text == "Я прочитал(-а)":
           question_before_quiz(message)

def are_you_sure(message):
    message_are_you_sure = f'Вы уверены?'
    #bot.send_message(message.chat.id,message_are_you_sure,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Да')
    itembtn2 = types.KeyboardButton('Нет, я передумал')
    markup.add(itembtn1, itembtn2 )
    if message.text == "Да":
        denied_question_before_quiz(message)
    else:
        bot.register_next_step_handler(message_are_you_sure,quiz)

    def bye_before_quiz(message):
    message = f' Хорошо. Уверена, что на моем аккаунте вы найдете еще много полезной информации 😉'
    bot.send_message(message.chat.id,message,parse_mode='html')

#bot





def question_before_quiz(call):
        message_before_quiz = f'Наверняка после прочтения у вас в мыслях уже начинает потихоньку зарождаться личный инвестиционный план.'\
            'Чтобы выстроить свою правильную финансовую модель и обеспечить комфортную жизнь себе и своим потомкам, нужно погрузиться в эту тему с головой. 👨‍💻'\
            '📝Об этом максимально подробно и попунктам мы рассказываем на курсе'\
            '- находим дополнительные источники дохода;- выбираем стратегии финансового роста- создаём систему планомерных накоплений- выстраиваем щит от потерь.'\
                
        bot.send_message(message.chat.id,message_before_quiz  ,parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Да')
        itembtn2 = types.KeyboardButton('Нет')
        markup.add(itembtn1, itembtn2 )
        bot.send_message(message.chat.id, "Хотите получить бесплатную консультацию от эксперта?", reply_markup=markup)
def get_sales(message):
    global user_data
    user_data = []
    lid_message = f'С вами свяжется мой помощник и расскажет все о курсе. Напишите ваш номер телефона'
    sent_get_message = bot.send_message(message.chat.id,lid_message,parse_mode='html')
    bot.register_next_step_handler(sent_get_message ,  get_user_phone)
@bot.message_handler()
def get_user_phone(message):
    global user_phone, pattern
    if re.fullmatch(pattern, message.text):
        get_user_name(message)
    else:
        msg = bot.send_message(message.chat.id, "Напишите номер в формате 8XXXXXXXXXX")
        bot.register_next_step_handler(msg,  get_user_phone)

def get_user_name(message):
            get_name = bot.send_message(message.chat.id,'Напишите ваше имя',parse_mode='html')
            user_phone = message.text
            user_data.append( user_phone )
            bot.register_next_step_handler(get_name,  say_bye)

def say_bye(message):
            bot.send_message(message.chat.id,'Спасибо за информацию. До свидания, с вами свяжется специалист',parse_mode='html')
            user_name = message.text
            user_data.append(user_name)
            print(user_data)
'''

    




bot.infinity_polling()


    