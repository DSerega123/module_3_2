def send_email(message, recipient, sender = "university.help@gmail.com"):
    if (recipient.find('@') == -1) or ((recipient.endswith(".com") == False) and (recipient.endswith(".ru") == False) and (recipient.endswith(".net") == False)) or (sender.find('@') == -1) or ((sender.endswith(".com") == False) and (sender.endswith(".ru") == False) and (sender.endswith(".net") == False)):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    else:
        if recipient is sender:
            print('Нельзя отправить письмо самому себе!')
        else:
            if "university.help@gmail.com" in sender:
                print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')