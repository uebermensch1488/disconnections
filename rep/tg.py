import telebot

from date import day_add

bot = telebot.TeleBot("1499593962:AAG5ObbcZsycM9O6M9wHD91Xi05b_mPsbTg")

def send_data_to_tg(results, sent_data_tg):
    for disconnection in results:
        if disconnection not in sent_data_tg:
            bot.send_message(1340073704, f'''
                {disconnection['region']}\n
                {disconnection['district']}\n
                {disconnection['location']}\n
                {disconnection['object']}\n
                {disconnection['disconn-start-date']}\n
                {disconnection['disconn-start-time']}\n
                {disconnection['disconn-end-date']}\n
                {disconnection['disconn-end-time']}\n
                {disconnection['branch']}\n
                {disconnection['res_title']}
                ''')
            sent_data_tg.append(disconnection)
    return sent_data_tg

def check_disconnection(results):
    dates = day_add()
    for disconnection in results:
        if disconnection["disconn-start-date"] == f'{dates[0]}' and disconnection["region"] == "д. Сидорово":
            bot.send_message(1340073704, "Завтра планируется отключение в деревне Сидорово")
        
        if disconnection["disconn-start-date"] == f'{dates[1]}' and disconnection["region"] == "д. Сидорово":
            bot.send_message(1340073704, "Через три дня планируется отключение в деревне Сидорово")
        
        if disconnection["disconn-start-date"] == f'{dates[2]}' and disconnection["region"] == "д. Сидорово":
            bot.send_message(1340073704, "Через неделю планируется отключение в деревне Сидорово")
