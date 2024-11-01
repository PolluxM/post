# Отправка электронной почты
import smtplib
from email.message import EmailMessage

sender_email = 'pelikhovmn@yandex.ru' # Почтовый ящик для отправки
recipient_mail = 'pelikhovmn@gmail.com' # Почтовый ящик для получения
password = 'wvluhemojpvgecal' # Пароль для использования через почтовый ящик (создается в профиле)
subject = 'Проверка связи' # Заголовок письма
body = 'Привет из программы на Питоне!' # Тело письма

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg["From"] = sender_email
msg["To"] = recipient_mail

try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(sender_email, password)
    server.send_message(msg)
    print('Письмо доставлено!')
except Exception as e:
    print(f'Ошибка: {e}')
finally:
    if server:
        server.quit()
